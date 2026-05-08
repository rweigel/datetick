# Create plots with varying time ranges.

import os
import matplotlib.pyplot as plt

from datetick import datetick

try:
  import pytest
except ImportError:
  print("pytest is required to run this test. Please install it with 'pip install pytest'")
  exit()


@pytest.mark.short
def test_one(debug=False):
  _run_all(short=True, debug=debug)


def test_all(debug=False):
  _run_all(dir='x', figwidth=4, debug=debug)


def _run_all(short=False, dir='x', figwidth=8, debug=False):
  import json

  test_file = os.path.join(_script_dir(), 'visual_test.json')
  with open(test_file, 'r') as file:
    tests = json.load(file)

  dirty = False
  for entries in tests.values():
    for test in entries:
      delta = _parse_ds(test['stop']) - _parse_ds(test['start'])
      dt_str = _fmt_delta(delta)
      if test.get('_delta_t') != dt_str:
        test['_delta_t'] = dt_str
        dirty = True
  if dirty:
    with open(test_file, 'w') as file:
      json.dump(tests, file, indent=2)

  files = []
  for test_cat in ['kwargs', 'main']:
    for test in tests[test_cat]:
      dt_str_o = test['start']
      dt_str_f = test['stop']
      kwargs = {k: v for k, v in test.items() if not k.startswith('_') and k not in ('start', 'stop')}
      _plot(dt_str_o, dt_str_f, dir=dir, figwidth=figwidth, debug=debug, **kwargs)
      file = _savefig(dt_str_o, dt_str_f, dir, files, debug=debug)
      files.append(file)
      if short:
        break

  if not short:
    _append_to_readme(files, dir, debug=debug)
    _create_subdir_readme(files, dir, debug=debug)


def _plot(ds1, ds2, dir='x', figwidth=8, **kwargs): 

  def _set_title(ax, dir, delta_t):
    if dir == 'x':
      newline = ''
      space = ''
    else:
      newline = '\n'
      space = '  '

    delta_t = _fmt_delta(delta_t)

    title = f"{ds1}/{newline}{space}{ds2}{newline} Δt = {delta_t}"
    ax.set_title(title, fontsize=10, fontfamily='monospace')


  def _axes(dir, figwidth):

    if dir == 'x':
      figsize=(figwidth, 2)
      hspace = 1.0
    else:
      figsize=(2, figwidth)
      hspace = 0.1

    fig, axes = plt.subplots(2, figsize=figsize)
    plt.subplots_adjust(hspace=hspace)
    for axis in axes:
      axis.grid()
      if dir == 'x':
        axis.spines[['top', 'right', 'left']].set_visible(False)
        axis.yaxis.set_visible(False)
      else:
        axis.spines[['top', 'right']].set_visible(False)

    return fig, axes


  def _set_label(ax, dir, x, y, text, datetick_kwargs=None):
    if dir == 'x':
      yt = 0.0
      xt = x[0] + (x[1] - x[0])/2
    if dir == 'y':
      xt = 0.5
      yt = y[0] + (y[1] - y[0])/2

    bbox = {
            'boxstyle': 'round,pad=0.3',
            'facecolor': 'white',
            'edgecolor': 'gray',
            'alpha': 0.8
    }

    if datetick_kwargs:
      bbox['facecolor'] = 'lightblue'
      for key, value in kwargs.items():
        if key == 'debug':
          continue
        text += f'\n{key}={value}'

    ax.text(xt, yt, text, ha='center', va='center', bbox=bbox, fontsize=9)


  fig, axes = _axes(dir, figwidth)

  dt1 = _parse_ds(ds1)
  dt2 = _parse_ds(ds2)
  if dir == 'x':
    x = [dt1, dt2]
    y = [0.0, 0.0]
  else:
    x = [0.0, 1.0]
    y = [dt1, dt2]

  axes[0].plot(x, y, '*')
  _set_label(axes[0], dir, x, y, 'matplotlib')

  axes[1].plot(x, y, '*')
  _set_label(axes[1], dir, x, y, 'datetick', datetick_kwargs=kwargs)

  cfg = datetick(dir, axes=axes[1], **kwargs)

  _set_title(axes[0], dir, cfg['delta_t'])

  return cfg


def _savefig(ds1, ds2, dir, files, debug=False):
  ds1 = ds1.replace(":","").replace("-","").replace("T","").replace("Z","")
  ds2 = ds2.replace(":","").replace("-","").replace("T","").replace("Z","")

  ext = 'svg'
  base = f'{_out_dir()}/{ds1}-{ds2}-{dir}'
  file = f'{base}.{ext}'
  if file in files:
    v = 2
    while file in files:
      file = f'{base}_v{v}.{ext}'
      v += 1

  if debug:
    print("Writing", file)
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


def _append_to_readme(files, dir, debug=False):

  readme = 'README.md' # Repo README
  readme = os.path.join(_script_dir(), "..", readme)

  with open(readme, 'r+') as file:
    lines = file.readlines()

  index = next(i for i, line in enumerate(lines) if "Comparison to default Matplotlib" in line)
  del lines[index+1:]

  latest_dir = os.path.join(_script_dir(), 'visual_test', 'latest')
  os.makedirs(latest_dir, exist_ok=True)

  # Add python/mpl version
  mpl = f"Matplotlib-{plt.matplotlib.__version__}"
  py = f"Python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  lines.append(f"\n\n<code>{py}/{mpl}</code>\n\n")

  image_links = []
  for file in files:
    latest_file = os.path.join(latest_dir, os.path.basename(file))
    # Copy file to test/visual_tests/latest for linking in README
    with open(file, 'rb') as src, open(latest_file, 'wb') as dst:
      dst.write(src.read())
    # Make path relative to README
    base = "https://raw.githubusercontent.com/rweigel/datetick/main/"
    file = os.path.relpath(latest_file, os.path.dirname(readme))
    image_links.append(f'![{file}]({base}{file})')

  lines.append(f"\n## <code>dir={dir}</code>\n\n")
  lines.append("\n\n".join(image_links))

  if debug:
    print(f"Updating {readme} with {len(files)} images")
  with open(readme, 'w') as file:
    file.writelines(lines)

  # Create README.rel.md with base replaced with relative path for local viewing
  readme_rel = os.path.join(os.path.dirname(readme), 'README.rel.md')
  if debug:
    print(f"Writing {readme_rel} with URL replaced by relative path")
  with open(readme_rel, 'w') as file:
    file.writelines(line.replace(base, "") for line in lines)


def _create_subdir_readme(files, dir, debug=False):
  # Create README in mpl subdir
  image_links = []
  for file in files:
    # Make path relative to README
    file = os.path.basename(file)
    image_links.append(f'![{file}]({file})')

  readme = os.path.join(_out_dir(), 'README.md')
  if debug:
    print(f"Writing {readme} with {len(files)} images")
  with open(readme, 'w') as file:
    file.writelines("\n" + "\n\n".join(image_links))


def _out_dir():
  mpl = f"mpl-{plt.matplotlib.__version__}"
  py = f"python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  return os.path.join(_script_dir(), 'visual_test', py, mpl)


def _script_dir():
  return os.path.dirname(os.path.realpath(__file__))


def _fmt_delta(td):
    total = td.total_seconds()
    days = td.days
    hours, rem = divmod(total - days * 86400, 3600)
    minutes, seconds = divmod(rem, 60)
    hours, minutes = int(hours), int(minutes)
    secs_int = int(seconds)
    micros = round((seconds - secs_int) * 1e6)

    parts = []
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


def _parse_ds(ds):
  import dateutil.parser
  return dateutil.parser.parse(ds)


if __name__ == '__main__':
  if True:
    dir = 'x'
    figwidth = 2
    ds1 = '2001-02-12T00:00:00Z'
    ds2 = '2002-01-31T00:00:00Z'
    file = _plot(ds1, ds2, dir, figwidth, debug=True)
    print("Writing", 'a.png')
    plt.savefig('a.png', bbox_inches='tight', dpi=300)
    plt.close()
    exit()

  #test_one(debug=True)
  test_all(debug=False)
