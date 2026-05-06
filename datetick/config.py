def config(deltaT, config=None, debug=False):
  import json
  import matplotlib
  import matplotlib.dates as mpld

  if config is None:
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, 'config.json')) as f:
      config = json.load(f)

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

  LOCATOR_MAP = {
    'YearLocator':        lambda c: mpld.YearLocator(c['base']),
    'MonthLocator':       lambda c: mpld.MonthLocator(bymonth=_arange(c, 'bymonth')),
    'DayLocator':         lambda c: mpld.DayLocator(bymonthday=_arange(c, 'bymonthday')),
    'HourLocator':        lambda c: mpld.HourLocator(byhour=_arange(c, 'byhour')),
    'MinuteLocator':      lambda c: mpld.MinuteLocator(byminute=_arange(c, 'byminute')),
    'SecondLocator':      lambda c: mpld.SecondLocator(bysecond=_arange(c, 'bysecond')),
    'MicrosecondLocator': lambda c: mpld.MicrosecondLocator(interval=c['interval'])
  }

  def make_locator(spec):
    if spec is None:
      return None
    return LOCATOR_MAP[spec['class']](spec)

  def make_formatter(spec):
    if spec is None:
      return None
    if spec['class'] == 'MillisecondFuncFormatter':
      return matplotlib.ticker.FuncFormatter(_millis)
    return mpld.DateFormatter(spec['format'])

  total_seconds = deltaT.total_seconds()
  for rule in config:
    threshold = rule['if_seconds_lt']
    if threshold is None or total_seconds < threshold:
        return {
        'major': make_locator(rule['major']),
        'minor': make_locator(rule['minor']),
        'fmt1':  make_formatter(rule['fmt1']),
        'fmt2':  rule['fmt2'],
        'trans': rule['trans']
      }


def _millis(x, pos):
  import matplotlib
  x = matplotlib.dates.num2date(x)
  label = x.strftime('.%f')
  label = label[0:3]
  return label


def config2(deltaT, debug=False):
  # Old code. Delete eventually.
  import matplotlib
  import matplotlib.dates as mpld

  nHours = deltaT.days * 24.0 + deltaT.seconds/3600.0
  if deltaT.total_seconds() < 0.1:
    # Locators don't locate at this resolution.
    # Use default Matplotlib locator and formatter, which will show fractional seconds.
    return {'major': None, 'minor': None, 'fmt1': None, 'fmt2': None, 'trans': None}
  elif deltaT.total_seconds() < 1:
    if debug:
      print('Using < 1 second locator')
    major = mpld.MicrosecondLocator(interval=100000)
    minor = mpld.MicrosecondLocator(interval=50000)
    fmt1 = matplotlib.ticker.FuncFormatter(_millis)
    fmt2  = '%H:%M:%S\n%Y-%m-%d'
    trans = 'second'
  elif deltaT.total_seconds() < 2:
    if debug:
      print('Using < 2 seconds locator')
    major = mpld.MicrosecondLocator(interval=250000)
    minor = mpld.MicrosecondLocator(interval=125000)
    fmt1 = matplotlib.ticker.FuncFormatter(_millis)
    fmt2  = '%H:%M:%S\n%Y-%m-%d'
    trans = 'second'
  elif deltaT.total_seconds() < 5:
    if debug:
      print('Using < 5 seconds locator')
    major = mpld.MicrosecondLocator(interval=500000)
    minor = mpld.MicrosecondLocator(interval=250000)
    fmt1 = matplotlib.ticker.FuncFormatter(_millis)
    fmt2  = '%H:%M:%S\n%Y-%m-%d'
    trans = 'second'
  elif deltaT.total_seconds() < 10:
    # < 10 seconds
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    minor = mpld.MicrosecondLocator(interval=500000)
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 20:
    # < 20 seconds
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 2)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 30:
    # < 30 seconds
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 5)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 1)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60:
    # < 1 minute
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 10)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 2)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60*2:
    # < 2 minutes
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 20)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60*3:
    # < 3 minutes
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 20)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60*5:
    # < 5 minutes
    major = mpld.SecondLocator(bysecond=list(range(0, 60, 30)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 10)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60*10:
    # < 10 minutes
    major = mpld.MinuteLocator(byminute=list(range(0, 60, 1)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 15)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60*20:
    # < 20 minutes
    major = mpld.MinuteLocator(byminute=list(range(0, 60, 2)) )
    minor = mpld.SecondLocator(bysecond=list(range(0, 60, 30)) )
    fmt1  = mpld.DateFormatter('%M:%S')
    fmt2  = '%Y-%m-%dT%H'
    trans = 'hour'
  elif deltaT.total_seconds() < 60*30:
    # < 30 minutes
    major = mpld.MinuteLocator(byminute=list(range(0, 60, 5)) )
    minor = mpld.MinuteLocator(byminute=list(range(0, 60, 1)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif deltaT.total_seconds() < 60*60:
    # < 60 minutes
    major = mpld.MinuteLocator(byminute=list(range(0, 60, 10)) )
    minor = mpld.MinuteLocator(byminute=list(range(0, 60, 2)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 2:
    major = mpld.MinuteLocator(byminute=list(range(0, 60, 15)) )
    minor = mpld.MinuteLocator(byminute=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 4:
    major = mpld.MinuteLocator(byminute=list(range(0, 60, 20)) )
    minor = mpld.MinuteLocator(byminute=list(range(0, 60, 5)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 6:
    major = mpld.HourLocator(byhour=list(range(0,24,1)) )
    minor = mpld.MinuteLocator(byminute=list(range(0, 60, 10)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 12:
    major = mpld.HourLocator(byhour=list(range(0,24,2)) )
    minor = mpld.MinuteLocator(byminute=list(range(0, 60, 30)) )
    fmt1  = mpld.DateFormatter('%H:%M')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 24:
    # < 1 day
    major = mpld.HourLocator(byhour=list(range(0, 24, 3)) )
    minor = mpld.HourLocator(byhour=list(range(0, 24, 1)) )
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 48:
    # < 2 days
    major = mpld.HourLocator(byhour=list(range(0, 24, 4)) )
    minor = mpld.HourLocator(byhour=list(range(0, 24, 2)) )
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 72:
    # < 3 days
    major = mpld.HourLocator(byhour = list(range(0, 24, 6)))
    minor = mpld.HourLocator(byhour = list(range(0, 24, 3)))
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif nHours < 96:
    # < 4 days
    major = mpld.HourLocator(byhour = list(range(0, 24, 12)))
    minor = mpld.HourLocator(byhour = list(range(0, 24, 3)))
    fmt1  = mpld.DateFormatter('%H')
    fmt2  = '%Y-%m-%d'
    trans = 'day'
  elif deltaT.days < 8:
    major = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    minor = mpld.HourLocator(byhour=list(range(0, 24, 4)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
    trans = 'month'
  elif deltaT.days < 16:
    major = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    minor = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
    trans = 'month'
  elif deltaT.days < 32:
    major = mpld.DayLocator(bymonthday=list(range(1, 32, 4)))
    minor = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
    trans = 'month'
  elif deltaT.days < 60:
    major = mpld.DayLocator(bymonthday=list(range(1, 32, 7)))
    minor = mpld.DayLocator(bymonthday=list(range(1, 32, 1)))
    fmt1  = mpld.DateFormatter('%d')
    fmt2  = '%Y-%m'
    trans = 'month'
  elif deltaT.days < 183:
    major = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    minor = mpld.DayLocator(bymonthday=list(range(1, 32, 7)))
    fmt1  = mpld.DateFormatter('%m')
    fmt2  = '%Y'
    trans = 'month'
  elif deltaT.days < 367:
    major = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    minor = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    fmt1  = mpld.DateFormatter('%m')
    fmt2  = '%Y'
    trans = 'month'
  elif deltaT.days < 366*2:
    major = mpld.MonthLocator(bymonth=list(range(1, 13, 2)))
    minor = mpld.MonthLocator(bymonth=list(range(1, 13, 1)))
    fmt1  = mpld.DateFormatter('%m')
    fmt2  = '%Y'
    trans = 'month'
  elif deltaT.days < 366*8:
    major = mpld.YearLocator(1)
    minor = mpld.MonthLocator(bymonth=list(range(1, 13, 4)))
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    trans = None
  elif deltaT.days < 366*15:
    major = mpld.YearLocator(1)
    minor = mpld.YearLocator(1)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    trans = None
  elif deltaT.days < 366*40:
    major = mpld.YearLocator(5)
    minor = mpld.YearLocator(1)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    trans = None
  elif deltaT.days < 366*100:
    major = mpld.YearLocator(10)
    minor = mpld.YearLocator(2)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    trans = None
  elif deltaT.days < 366*200:
    major = mpld.YearLocator(20)
    minor = mpld.YearLocator(5)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    trans = None
  else:
    major = mpld.YearLocator(50)
    minor = mpld.YearLocator(10)
    fmt1  = mpld.DateFormatter('%Y')
    fmt2  = ''
    trans = None

  return {'major': major, 'minor': minor, 'fmt1': fmt1, 'fmt2': fmt2, 'trans': trans}