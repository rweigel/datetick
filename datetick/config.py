def config(deltaT, config=None, debug=False):
  import json
  import warnings

  if config is None:
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'config.json')) as f:
      config = json.load(f)

  _validate_config(config)

  total_seconds = deltaT.total_seconds()
  for rule in config:
    rng = rule['range']
    lo = _to_seconds(rng.get('min'))
    hi = _to_seconds(rng.get('max'))
    lo = lo if lo is not None else 0
    if lo <= total_seconds and (hi is None or total_seconds < hi):
      major = rule['major']
      minor = rule['minor']
      return {
        'major_locator':    _make_locator(major['locator'] if major else None),
        'minor_locator':    _make_locator(minor['locator'] if minor else None),
        'major_formatter':  _make_formatter(major.get('formatter') if major else None),
        'minor_formatter':  _make_formatter(minor.get('formatter') if minor else None),
        'major_sub_format': rule.get('major_sub_format', ''),
        'trans':            rule['trans']
      }

  warnings.warn(f"No matching config rule found for deltaT={deltaT}; returning None.")

  return None


def _make_locator(spec):
  import matplotlib.dates as mpld
  if spec is None:
    return None
  LOCATOR_MAP = {
    'YearLocator':        lambda c: mpld.YearLocator(c['base']),
    'MonthLocator':       lambda c: mpld.MonthLocator(bymonth=_arange(c, 'bymonth')),
    'DayLocator':         lambda c: mpld.DayLocator(bymonthday=_arange(c, 'bymonthday')),
    'HourLocator':        lambda c: mpld.HourLocator(byhour=_arange(c, 'byhour')),
    'MinuteLocator':      lambda c: mpld.MinuteLocator(byminute=_arange(c, 'byminute')),
    'SecondLocator':      lambda c: mpld.SecondLocator(bysecond=_arange(c, 'bysecond')),
    'MicrosecondLocator': lambda c: mpld.MicrosecondLocator(interval=c['interval'])
  }
  return LOCATOR_MAP[spec['class']](spec)


def _make_formatter(spec):
  import matplotlib
  if spec is None:
    return None
  if spec['class'] == 'MillisecondFuncFormatter':
    return matplotlib.ticker.FuncFormatter(_millis)
  return matplotlib.dates.DateFormatter(spec['format'])


def _validate_config(config):
  """Validate that config is well-formed."""
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
      "formatter": formatter_spec
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
      "required": ["range", "major", "trans"],
      "properties": {
        "comment": {"type": "string"},
        "range": {
          "type": "object",
          "required": ["min", "max"],
          "properties": {
            "comment": {"type": "string"},
            "min": {"type": "object"},
            "max": {"type": "object"}
          },
          "additionalProperties": False
        },
        "major": {"oneOf": [major_spec, {"type": "null"}]},
        "minor": {"oneOf": [minor_spec, {"type": "null"}]},
        "major_sub_format": {"type": ["string", "null"]},
        "trans": {"type": ["string", "null"]}
      }
    }
  }
  try:
    jsonschema.validate(instance=config, schema=schema)
  except jsonschema.exceptions.ValidationError as e:
    raise ValueError(f"Config validation error: {e.message}")

  _validate_ranges(config)


def _validate_ranges(config):
  """Validate that config ranges are non-overlapping and cover all positive deltas."""
  ranges = []
  for rule in config:
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


def _arange(spec, key):
  """Return list from key or key_arange ([start, stop] or [start, stop, step], stop exclusive).
  If both exist, warn and use key."""
  arange_key = key + '_arange'
  has_key = key in spec
  has_arange = arange_key in spec
  if has_key and has_arange:
    import warnings
    warnings.warn(f"Both '{key}' and '{arange_key}' specified; using '{key}'.")
  if has_key:
    return spec[key]
  if has_arange:
    return list(range(*spec[arange_key]))
  raise KeyError(f"Neither '{key}' nor '{arange_key}' found in locator spec.")


def _to_seconds(spec):
  """Convert {'unit': value} to total seconds. Returns None if spec is None."""
  UNIT_SECONDS = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}
  if spec is None:
    return None
  unit, value = next(iter(spec.items()))
  return value * UNIT_SECONDS[unit]


def _millis(x, pos):
  import matplotlib
  x = matplotlib.dates.num2date(x)
  label = x.strftime('.%f')
  label = label[0:3]
  return label
