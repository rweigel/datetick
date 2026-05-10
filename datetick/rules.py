def rule(delta_t, rule_idx=None, rules_file=None, debug=False):
  import os
  import json


  """
  major_sub_format contains additional information that is used for the first
   tick label or when there is a major change. For example, if
    major_format = %M:%S and major_sub_format = %H,
  the labels will have only minute and hour and the first tick will have a
  label of %M:%S\n%H. If there is a change in hour somewhere on the axis,
  that label will include the new hour.

  Note that interval=... is specified even when it would seem to be redundant.
  It is needed to workaround the bug discussed at stackoverflow.com/q/31072589
  """

  if rules_file is None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rules_file = os.path.join(script_dir, 'rules.json')

  if not os.path.exists(rules_file):
    raise FileNotFoundError(f"Could not find rules file at {rules_file}")

  with open(rules_file) as f:
    try:
      rules = json.load(f)
    except json.JSONDecodeError as e:
      raise ValueError(f"Error parsing rules file: {e}")

  # Validate and set defaults for optional fields in rules
  rules = _validate_rules(rules)

  total_seconds = delta_t.total_seconds()
  for matched_index, matched_rule in enumerate(rules):
    rng = matched_rule['range']
    lo = _to_seconds(rng.get('min'))
    hi = _to_seconds(rng.get('max'))
    lo = lo if lo is not None else 0
    if lo <= total_seconds and (hi is None or total_seconds < hi):
      if isinstance(rule_idx, int):
        target_index = matched_index + rule_idx
        if target_index < 0:
          return rules[0]
        if target_index >= len(rules):
          return rules[-1]
        return rules[target_index]
      return matched_rule

  #warnings.warn(f"No matching config rule found for delta_t={delta_t}; returning None.")

  if debug:
    delta_t_str = util.format_delta(delta_t)
    print(f'Rule for delta_t = {delta_t_str}:')
    for key, value in rule.items():
      print(f'  {key}: {value}')

  return None


def _validate_rules(rules):
  """Validate that config is well-formed."""

  import copy
  import jsonschema

  locator_spec = {
    "type": "object",
    "required": ["class"],
    "properties": {
      "class": {"type": "string"}
    }
  }

  formatter_spec = {
    "type": "object",
    "required": ["class"],
    "properties": {
      "class": {"type": "string"},
      "format": {"type": "string"}
    }
  }

  major_spec = {
    "type": "object",
    "required": ["locator"],
    "properties": {
      "locator":   locator_spec,
      "formatter": formatter_spec,
      "sub_format": {"type": ["string", "null"]},
      "sub_transition": {"type": ["string", "null"]}
    },
    "additionalProperties": False
  }

  minor_spec = {
    "type": "object",
    "required": ["locator"],
    "properties": {
      "locator":   locator_spec,
      "formatter": formatter_spec
    },
    "additionalProperties": False
  }

  schema = {
    "type": "array",
    "items": {
      "type": "object",
      "required": ["range", "major"],
      "properties": {
        "comment": {"type": "string"},
        "range": {
          "type": "object",
          "required": ["min", "max"],
          "properties": {
            "comment": {"type": "string"},
            "min": {"type": ["object", "null"]},
            "max": {"type": ["object", "null"]}
          },
          "additionalProperties": False
        },
        "major": {"oneOf": [major_spec, {"type": "null"}]},
        "minor": {"oneOf": [minor_spec, {"type": "null"}]}
      }
    }
  }

  try:
    jsonschema.validate(instance=rules, schema=schema)
  except jsonschema.exceptions.ValidationError as e:
    raise ValueError(f"Config validation error: {e.message}")

  rules = copy.deepcopy(rules)

  # Set defaults for optional fields
  for rule in rules:

    if rule['major'] is None:
      rule['major'] = {'locator': None, 'formatter': None, 'sub_format': None, 'sub_transition': None}
    if 'minor' not in rule or rule['minor'] is None:
      rule['minor'] = {'locator': None, 'formatter': None}

    for part in ['major', 'minor']:
      if 'locator' not in rule[part]:
        rule[part]['locator'] = None
      if 'formatter' not in rule[part]:
        rule[part]['formatter'] = None
    if 'sub_format' not in rule['major']:
      rule['major']['sub_format'] = None
    if 'sub_transition' not in rule['major']:
      rule['major']['sub_transition'] = None

    if 'major_sub_format' in rule and rule['major']['sub_format'] is None:
      rule['major']['sub_format'] = rule.pop('major_sub_format')
    elif 'major_sub_format' in rule:
      rule.pop('major_sub_format')
    if 'major_sub_transition' in rule and rule['major']['sub_transition'] is None:
      rule['major']['sub_transition'] = rule.pop('major_sub_transition')
    elif 'major_sub_transition' in rule:
      rule.pop('major_sub_transition')

  _validate_ranges(rules)

  return rules


def _validate_ranges(rules):
  """Validate that config ranges are non-overlapping and cover all positive deltas."""
  ranges = []
  for rule in rules:
    if 'range' in rule:
      rng = rule['range']
      lo = _to_seconds(rng.get('min')) if 'min' in rng else 0
      hi_val = _to_seconds(rng.get('max')) if 'max' in rng else None
      hi = hi_val if hi_val is not None else float('inf')
      if lo < 0 or hi <= lo:
        raise ValueError(f"Invalid range: {rng}")
      ranges.append((lo, hi))

  ranges.sort()
  for i in range(1, len(ranges)):
    if ranges[i][0] < ranges[i-1][1]:
      raise ValueError(f"Overlapping ranges: {ranges[i-1]} and {ranges[i]}")
    if ranges[i][0] > ranges[i-1][1]:
      raise ValueError(f"Gap in ranges: {ranges[i-1]} and {ranges[i]}")
  if ranges[0][0] > 0:
    raise ValueError(f"Ranges do not cover all positive deltas: first range starts at {ranges[0][0]} seconds")


def _to_seconds(spec):
  """Convert {'unit': value} to total seconds. Returns None if spec is None."""
  UNIT_SECONDS = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}
  if spec is None:
    return None
  unit, value = next(iter(spec.items()))
  return value * UNIT_SECONDS[unit]
