import datetick

def generate_main_tests():
  import datetime

  base_start = datetime.datetime(2001, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
  generated = []
  seen = set()

  rules = datetick.rules.rules()

  for rule in rules:
    major = rule.get('major')
    locator_spec = None if major is None else major.get('locator')
    if locator_spec is None:
      continue

    ticks = _major_tick_datetimes(locator_spec, rule['range'], base_start)
    deltas = _rule_deltas_from_ticks(ticks, rule['range'])

    for delta_t in deltas:
      for test in _transition_tests(base_start, delta_t):
        key = (test['start'], test['stop'], test.get('_comment'))
        if key in seen:
          continue
        seen.add(key)
        generated.append(test)

  generated.sort(key=lambda test: (parse_ds(test['stop']) - parse_ds(test['start']), test['start'], test['stop'], test.get('_comment', '')))
  return generated


def parse_ds(ds):
  import dateutil.parser
  return dateutil.parser.parse(ds)


def _format_ds(dt):
  dt = dt.astimezone(dt.tzinfo)
  text = dt.isoformat(timespec='microseconds').replace('+00:00', 'Z')
  base, frac = text.split('.')
  frac = frac[:-1].rstrip('0')
  if frac == '':
    frac = '0'
  return f'{base}.{frac}Z'


def _major_tick_datetimes(locator_spec, range_spec, base_start):
  import datetime
  import matplotlib.dates

  locator = datetick.util.make_locator(locator_spec)
  window_stop = _tick_window_stop(base_start, range_spec, locator_spec)
  tick_values = locator.tick_values(base_start, window_stop)

  ticks = []
  for value in tick_values:
    tick = matplotlib.dates.num2date(value)
    tick = tick.astimezone(datetime.timezone.utc).replace(tzinfo=datetime.timezone.utc)
    ticks.append(tick)

  return sorted(set(ticks))


def _rule_deltas_from_ticks(ticks, range_spec):
  min_seconds = _range_seconds(range_spec.get('min'))
  max_seconds = _range_seconds(range_spec.get('max'))
  deltas = {}

  for i, tick_start in enumerate(ticks):
    for tick_stop in ticks[i+1:]:
      delta_t = tick_stop - tick_start
      seconds = delta_t.total_seconds()
      if seconds < min_seconds:
        continue
      if max_seconds is not None and seconds >= max_seconds:
        break
      deltas[round(seconds, 6)] = delta_t

  return [deltas[key] for key in sorted(deltas)]


def _transition_tests(base_start, delta_t):
  import datetime

  tests = []

  def add_test(start, stop, comment=None):
    test = {
      'start': _format_ds(start),
      'stop': _format_ds(stop),
      '_delta_t': datetick.util.format_delta(stop - start)
    }
    if comment is not None:
      test['_comment'] = comment
    tests.append(test)

  add_test(base_start, base_start + delta_t)

  boundaries = [
    ('second', datetime.timedelta(seconds=1), datetime.datetime(2001, 1, 1, 0, 0, 1, tzinfo=datetime.timezone.utc)),
    ('minute', datetime.timedelta(minutes=1), datetime.datetime(2001, 1, 1, 0, 1, 0, tzinfo=datetime.timezone.utc)),
    ('hour', datetime.timedelta(hours=1), datetime.datetime(2001, 1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)),
    ('day', datetime.timedelta(days=1), datetime.datetime(2001, 1, 2, 0, 0, 0, tzinfo=datetime.timezone.utc)),
    ('month', datetime.timedelta(days=32), datetime.datetime(2001, 2, 1, 0, 0, 0, tzinfo=datetime.timezone.utc))
  ]

  for unit, threshold, boundary in boundaries:
    if delta_t >= threshold:
      continue

    offset = min(delta_t / 10, threshold / 10)
    start = boundary - delta_t + offset
    stop = boundary + offset
    add_test(start, stop, f'Cross {unit} boundary')

  return tests


def _tick_window_stop(base_start, range_spec, locator_spec):
  import datetime

  max_seconds = _range_seconds(range_spec.get('max'))
  unit, value = _locator_step(locator_spec)

  if max_seconds is not None:
    if unit in ('months', 'years'):
      min_stop = _locator_stop_for_steps(base_start, unit, value, 4)
      max_stop = base_start + datetime.timedelta(seconds=max_seconds)
      return max(min_stop, max_stop)

    step_seconds = max(value, 1e-6)
    window_seconds = max(max_seconds, step_seconds * 4) + step_seconds
    return base_start + datetime.timedelta(seconds=window_seconds)

  return _locator_stop_for_steps(base_start, unit, value, 6)


def _locator_stop_for_steps(base_start, unit, value, steps):
  import datetime

  if unit == 'years':
    return _add_years(base_start, value * steps)
  if unit == 'months':
    return _add_months(base_start, value * steps)
  return base_start + datetime.timedelta(seconds=value * steps)


def _locator_step(locator_spec):
  locator_class = locator_spec['class']

  if locator_class == 'MicrosecondLocator':
    return 'seconds', locator_spec['interval'] / 1_000_000
  if locator_class == 'SecondLocator':
    return 'seconds', _sequence_step(locator_spec, 'bysecond')
  if locator_class == 'MinuteLocator':
    return 'seconds', 60 * _sequence_step(locator_spec, 'byminute')
  if locator_class == 'HourLocator':
    return 'seconds', 3600 * _sequence_step(locator_spec, 'byhour')
  if locator_class == 'DayLocator':
    return 'seconds', 86400 * _sequence_step(locator_spec, 'bymonthday')
  if locator_class == 'MonthLocator':
    return 'months', _sequence_step(locator_spec, 'bymonth')
  if locator_class == 'YearLocator':
    return 'years', locator_spec['base']

  raise ValueError(f'Unsupported locator class: {locator_class}')


def _sequence_step(spec, key):
  arange_key = key + '_arange'
  if key in spec:
    values = spec[key]
  elif arange_key in spec:
    values = list(range(*spec[arange_key]))
  else:
    raise KeyError(f"Neither '{key}' nor '{arange_key}' found in locator spec.")

  if len(values) <= 1:
    return 1

  steps = sorted({values[i+1] - values[i] for i in range(len(values)-1) if values[i+1] > values[i]})
  if not steps:
    return 1
  return steps[0]


def _range_seconds(spec):
  if spec is None:
    return None

  unit, value = next(iter(spec.items()))
  unit_seconds = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400
  }

  if unit not in unit_seconds:
    raise ValueError(f'Unsupported range unit: {unit}')

  return value * unit_seconds[unit]


def _add_months(dt, months):
  import calendar

  month_index = dt.month - 1 + months
  year = dt.year + month_index // 12
  month = month_index % 12 + 1
  day = min(dt.day, calendar.monthrange(year, month)[1])
  return dt.replace(year=year, month=month, day=day)


def _add_years(dt, years):
  import calendar

  year = dt.year + years
  day = min(dt.day, calendar.monthrange(year, dt.month)[1])
  return dt.replace(year=year, day=day)
