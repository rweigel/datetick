# Create plots with varying time ranges.

import os
import matplotlib.pyplot as plt

import datetick

DIRS = ['x']
#FIGWIDTHS = [6.5, 3.25]
#FIGWIDTHS = [1.25]
FIGWIDTHS = [6.5]

# Print debug info for this script.
debug_script = True

try:
  import pytest
except ImportError:
  print("pytest is required to run this test. Please install it with 'pip install pytest'")
  exit()


@pytest.mark.short
def test_one(debug=False):
  _run_all(short=True, axis=DIRS[0], figwidth=FIGWIDTHS[0], debug=debug)


def test_all(debug=False):

  for axis in DIRS:
    files = {axis: []}
    for figwidth in FIGWIDTHS:
      if debug_script:
        print(f"Running visual test with axis='{axis}' and figwidth={figwidth}in")
      files[axis] += _run_all(axis=axis, figwidth=figwidth, debug=debug)

    #files[axis] = sorted(files[axis])

  _readmes(files, debug=debug)


def _run_all(short=False, axis='x', figwidth=8, debug=False):
  import json

  test_file = os.path.join(_script_dir(), 'visual_test.json')
  rules_file = os.path.join(_script_dir(), '..', 'datetick', 'rules.json')

  with open(test_file, 'r') as file:
    tests = json.load(file)
  with open(rules_file, 'r') as file:
    rules = json.load(file)

  generated_main = _generate_main_tests(rules)

  dirty_main = tests.get('main') != generated_main
  if dirty_main:
    tests['main'] = generated_main

  dirty_tests = False
  for test in tests.get('kwargs', []):
    delta = _parse_ds(test['stop']) - _parse_ds(test['start'])
    dt_str = datetick.util.format_delta(delta)
    if test.get('_delta_t') != dt_str:
      test['_delta_t'] = dt_str
      dirty_tests = True

  if dirty_main or dirty_tests:
    with open(test_file, 'w') as file:
      json.dump(tests, file, indent=2)

  files = []
  for entries in [tests.get('kwargs', []), tests.get('main', [])]:
    for test in entries:
      dt_str_o = test['start']
      dt_str_f = test['stop']
      kwargs = {k: v for k, v in test.items() if not k.startswith('_') and k not in ('start', 'stop')}

      if debug_script:
        print(f"delta_t={test['_delta_t']} | start={dt_str_o} | stop={dt_str_f} | kwargs={kwargs}")

      _plot(dt_str_o, dt_str_f, axis=axis, figwidth=figwidth, warn_on_min_gap=True, debug=debug, **kwargs)

      file = _savefig(dt_str_o, dt_str_f, axis, figwidth, files, debug=debug)
      files.append(file)

      if short:
        break

  return files


def _plot(ds1, ds2, axis='x', figwidth=6.5, **kwargs):

  def _set_title(ax, axis, delta_t):
    if axis == 'x':
      newline = ''
      space = ''
    else:
      newline = '\n'
      space = '  '

    delta_t = datetick.util.format_delta(delta_t)

    title = f"{ds1}/{newline}{space}{ds2}{newline} | Δt={delta_t} | w={figwidth}in"
    ax.set_title(title, fontsize=10, fontfamily='monospace')


  def _axes(axis, figwidth):

    if axis == 'x':
      figsize=(figwidth, 2)
      hspace = 1.0
    else:
      figsize=(2, figwidth)
      hspace = 0.1

    fig, axes = plt.subplots(2, figsize=figsize)
    plt.subplots_adjust(hspace=hspace)
    for ax in axes:
      ax.grid()
      if axis == 'x':
        ax.spines[['top', 'right', 'left']].set_visible(False)
        ax.yaxis.set_visible(False)
      else:
        ax.spines[['top', 'right']].set_visible(False)

    return fig, axes


  def _set_label(ax, axis, x, y, text, datetick_kwargs=None):
    axis_lims = ax.get_xlim() if axis == 'x' else ax.get_ylim()
    if axis == 'x':
      yt = 0.0
      xt = axis_lims[0] + (axis_lims[1] - axis_lims[0])/2
    if axis == 'y':
      xt = 0.5
      yt = axis_lims[0] + (axis_lims[1] - axis_lims[0])/2

    bbox = {
            'boxstyle': 'round,pad=0.3',
            'facecolor': 'white',
            'edgecolor': 'gray',
            'alpha': 0.8
    }

    if datetick_kwargs:
      bbox['facecolor'] = 'lightblue'
      for key, value in kwargs.items():
        if key in ('debug', 'warn_on_min_gap'):
          continue
        text += f'\n{key}={value}'

    ax.text(xt, yt, text, ha='center', va='center', bbox=bbox, fontsize=9)


  fig, axes = _axes(axis, figwidth)

  dt1 = _parse_ds(ds1)
  dt2 = _parse_ds(ds2)
  if axis == 'x':
    x = [dt1, dt2]
    y = [0.0, 0.0]
  else:
    x = [0.0, 1.0]
    y = [dt1, dt2]

  axes[0].plot(x, y, '*')
  _set_label(axes[0], axis, x, y, 'matplotlib')

  axes[1].plot(x, y, '*')
  _set_label(axes[1], axis, x, y, 'datetick', datetick_kwargs=kwargs)

  cfg = datetick.datetick(axis, axes=axes[1], **kwargs)

  _set_title(axes[0], axis, cfg['delta_t'])

  return cfg


def _savefig(ds1, ds2, axis, figwidth, files, debug=False):
  ds1 = ds1.replace(":","").replace("-","").replace("T","").replace("Z","")
  ds2 = ds2.replace(":","").replace("-","").replace("T","").replace("Z","")

  ext = 'svg'
  base = f'{_out_dir(axis)}/{ds1}-{ds2}-{figwidth}in'
  file = f'{base}.{ext}'
  if file in files:
    v = 2
    while file in files:
      file = f'{base}_v{v}.{ext}'
      v += 1

  if debug_script:
    print("  Writing", file)
  dirname = os.path.dirname(file)
  if not os.path.exists(dirname):
    os.makedirs(dirname, exist_ok=True)
  kwargs = {'bbox_inches': 'tight'}

  rc = {}
  if ext == 'png':
    kwargs['dpi'] = 220
    plt.savefig(file, **kwargs)
  else:
    if ext == 'svg':
      # Don't convert text to paths in SVG to keep it searchable and selectable
      kwargs['metadata'] = {"Date": None}  # Remove creation date for testing
      rc = {'svg.fonttype': 'none', 'svg.hashsalt': '67'}

  with plt.rc_context(rc):
    plt.savefig(file, **kwargs)

  plt.close()

  return file


def _generate_main_tests(rules_content):
  import datetime

  base_start = datetime.datetime(2001, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
  generated = []
  seen = set()

  for rule in rules_content:
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

  generated.sort(key=lambda test: (_parse_ds(test['stop']) - _parse_ds(test['start']), test['start'], test['stop'], test.get('_comment', '')))
  return generated


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


def _format_ds(dt):
  dt = dt.astimezone(dt.tzinfo)
  text = dt.isoformat(timespec='microseconds').replace('+00:00', 'Z')
  base, frac = text.split('.')
  frac = frac[:-1].rstrip('0')
  if frac == '':
    frac = '0'
  return f'{base}.{frac}Z'


def _readmes(files, debug=False):

  def _image_subsection(files, latest_dir, base, axis):
    image_links = []
    for file in files:
      # Copy file to test/visual_tests/latest for linking in README
      latest_file = os.path.join(latest_dir, os.path.basename(file))
      with open(file, 'rb') as src, open(latest_file, 'wb') as dst:
        dst.write(src.read())

      # Make path relative to README dir
      file = os.path.relpath(latest_file, os.path.dirname(readme))
      image_links.append(f'![{file}]({base}{file})')

    #size_axis = 'w' if axis == 'x' else 'h'
    #size_str = f"<code>{size_axis} = {size}in</code>"
    axis_str = f"<code>axis={axis}</code>"
    #section_header = f"\n## {axis_str} {size_str}\n\n"
    section_header = f"\n## {axis_str}\n\n"
    return section_header + "\n\n".join(image_links)

  readme = 'README.md' # Repo README
  readme = os.path.join(_script_dir(), "..", readme)

  with open(readme, 'r+') as file:
    lines = file.readlines()

  section_header = "Comparison to default `Matplotlib`"
  if not any(section_header in line for line in lines):
    raise ValueError(f"Could not find '{section_header}' section in README.md")

  index = next(i for i, line in enumerate(lines) if section_header in line)
  del lines[index+1:]

  # Add python/mpl version
  mpl = f"Matplotlib-{plt.matplotlib.__version__}"
  py = f"Python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  image_lines = []
  lines.append(f"\n\n<code>{py}/{mpl}</code>\n\n")

  base = "https://raw.githubusercontent.com/rweigel/datetick/main/"
  latest_dir = os.path.join(_script_dir(), 'visual_test', 'latest')
  os.makedirs(latest_dir, exist_ok=True)

  for axis in files.keys():
    image_lines.append(_image_subsection(files[axis], latest_dir, base, axis))

  combined_lines = lines + image_lines
  if debug_script:
    print(f"\nUpdating {readme} with {len(files[axis])} images")
  with open(readme, 'w') as file:
    file.writelines(combined_lines)

  # Create README.rel.md with base replaced with relative path for local viewing
  readme_rel = os.path.join(os.path.dirname(readme), 'README.rel.md')
  if debug_script:
    print(f"Writing {readme_rel} with URL replaced by relative path")
  with open(readme_rel, 'w') as file:
    file.writelines(line.replace(base, "") for line in combined_lines)

  readme = os.path.join(_out_dir(axis), 'README.md')
  if debug_script:
    print(f"Writing {readme} with {len(files[axis])} images")
  with open(readme, 'w') as file:
    file.writelines("\n" + "\n\n".join(image_lines))


def _out_dir(axis):
  mpl = f"mpl-{plt.matplotlib.__version__}"
  py = f"python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  return os.path.join(_script_dir(), 'visual_test', py, mpl, axis)


def _script_dir():
  return os.path.dirname(os.path.realpath(__file__))


def _parse_ds(ds):
  import dateutil.parser
  return dateutil.parser.parse(ds)


if __name__ == '__main__':
  def unit():
    ds1 = '2001-01-29T12:36:00.0Z'
    ds2 = '2001-02-01T06:36:00.0Z'
    _plot(ds1, ds2, axis='x', figwidth=6.5, adjust_range=False, debug=True)
    print("Writing", 'a.png')
    plt.savefig('a.png', bbox_inches='tight', dpi=300)
    plt.close()

  import sys
  if sys.argv[-1] == 'short':
    test_one(debug=True)
  elif sys.argv[-1] == 'unit':
    unit()
  else:
    test_all(debug=False)
