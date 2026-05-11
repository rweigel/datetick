# Create plots with varying time ranges.

import os
import matplotlib.pyplot as plt

import datetick

# Import ./util.py test functions for generating test cases
import util

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

  with open(test_file, 'r') as file:
    tests_manual = json.load(file)

  tests_generated = util.generate_main_tests()

  files = []
  for entries in [tests_manual, tests_generated]:
    for test in entries:
      dt_str_o = test['start']
      dt_str_f = test['stop']

      # Keep only 
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

  dt1 = util.parse_ds(ds1)
  dt2 = util.parse_ds(ds2)
  if axis == 'x':
    x = [dt1, dt2]
    y = [0.0, 0.0]
  else:
    x = [0.0, 1.0]
    y = [dt1, dt2]

  from matplotlib import dates as mdates

  if False:
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    axes[0].xaxis.set_major_locator(locator)
    axes[0].xaxis.set_major_formatter(formatter)

  axes[0].plot(x, y, '*')
  _set_label(axes[0], axis, x, y, 'matplotlib')

  axes[1].plot(x, y, '*')
  _set_label(axes[1], axis, x, y, 'datetick', datetick_kwargs=kwargs)

  cfg = datetick.datetick(axis, axes=axes[1], **kwargs)

  _set_title(axes[0], axis, cfg['delta_t'])

  return cfg


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


def _out_dir(axis):
  mpl = f"mpl-{plt.matplotlib.__version__}"
  py = f"python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  return os.path.join(_script_dir(), 'visual_test', py, mpl, axis)


def _script_dir():
  return os.path.dirname(os.path.realpath(__file__))


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
