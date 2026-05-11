import matplotlib


def make_locator(spec):

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

  if spec is None:
    return None
  LOCATOR_MAP = {
    'YearLocator':        lambda c: matplotlib.dates.YearLocator(c['base']),
    'MonthLocator':       lambda c: matplotlib.dates.MonthLocator(bymonth=_arange(c, 'bymonth')),
    'DayLocator':         lambda c: matplotlib.dates.DayLocator(bymonthday=_arange(c, 'bymonthday')),
    'HourLocator':        lambda c: matplotlib.dates.HourLocator(byhour=_arange(c, 'byhour')),
    'MinuteLocator':      lambda c: matplotlib.dates.MinuteLocator(byminute=_arange(c, 'byminute')),
    'SecondLocator':      lambda c: matplotlib.dates.SecondLocator(bysecond=_arange(c, 'bysecond')),
    'MicrosecondLocator': lambda c: matplotlib.dates.MicrosecondLocator(interval=c['interval'])
  }
  return LOCATOR_MAP[spec['class']](spec)


def make_formatter(spec):

  def _millis(x, pos):
    x = matplotlib.dates.num2date(x)
    label = x.strftime('.%f')
    label = label[0:3]
    return label

  if spec is None:
    return None
  if spec['class'] == 'MillisecondFuncFormatter':
    return matplotlib.ticker.FuncFormatter(_millis)
  return matplotlib.dates.DateFormatter(spec['format'])


def warn(msg):
  import warnings
  old_formatwarning = warnings.formatwarning
  def formatwarning(message, category, filename, lineno, line=None):
    return f'{filename}:{lineno}: {category.__name__}: {message}\n'
  warnings.formatwarning = formatwarning
  warnings.warn(msg)
  warnings.formatwarning = old_formatwarning


def get_ticks(axis, axes):
  if axis == 'x':
    return axes.get_xticks()
  else:
    return axes.get_yticks()


def get_ticklabels(axis, axes, strings=True):
  if axis == 'x':
    if strings:
      return [item.get_text() for item in axes.get_xticklabels()]
    return axes.get_xticklabels()
  else:
    if strings:
      return [item.get_text() for item in axes.get_yticklabels()]
    return axes.get_yticklabels()


def format_delta(delta, include_years=True):

  total = delta.total_seconds()
  days = delta.days
  hours, rem = divmod(total - days * 86400, 3600)
  minutes, seconds = divmod(rem, 60)
  hours, minutes = int(hours), int(minutes)
  secs_int = int(seconds)
  micros = round((seconds - secs_int) * 1e6)

  parts = []
  if include_years and days >= 366:
    years = days // 365.2425
    parts.append(f'{years:.1f}y')
  else:
    if days:
      parts.append(f'{days}d')
    if hours:
      parts.append(f'{hours}h')
    if minutes:
      parts.append(f'{minutes}m')
    if micros:
      parts.append(f'{secs_int}.{str(micros).zfill(6).rstrip("0")}s')
    elif secs_int:
      parts.append(f'{secs_int}s')

  return ''.join(parts) or '0s'


def print_ticks(axis, axes, ticks, labels):
  lim = axes.get_xlim() if axis == 'x' else axes.get_ylim()
  for i in range(0, len(ticks)):
    note = ''
    if ticks[i] < lim[0] or ticks[i] > lim[1]:
      note = ' (may be clipped by mpl b/c outside of axis limits)'
    label = str(labels[i]).replace("\n", "\\n")
    print(f' {label}    {matplotlib.dates.num2date(ticks[i])} {note}')


def backend_is_interactive(matplotlib_module=None):

  if matplotlib_module is None:
    import matplotlib as matplotlib_module

  backend = matplotlib_module.get_backend()
  if backend is None:
    return False
  return backend.lower() in {name.lower() for name in matplotlib.rcsetup.interactive_bk}
