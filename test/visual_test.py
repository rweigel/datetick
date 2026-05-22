# Create plots with varying time ranges.

import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot

import datetick

# Import ./util.py test functions for generating test cases
import util

# Print debug info for this script.
DEBUG_SCRIPT = False

# Maximum number of test cases to run.
N_MAX = float('inf')

#DIRS = ['x, y']
DIRS = ['x']
#FIGWIDTHS = [9.6, 6.4, 3.2, 1.6]
#FIGWIDTHS = [1.6]
#FIGWIDTHS = [3.2]
FIGWIDTHS = [6.4]
#FIGWIDTHS = [9.6]
FIGFMT = 'png'
OPEN_FIG = False
SHOW_FIG = False


try:
  import pytest
except ImportError:
  pytest = None


if pytest is None:
  def _short_mark(func):
    return func
else:
  _short_mark = pytest.mark.short


@_short_mark
def test_one(debug=False):
  test_all(debug=False, idx=1)


def test_all(debug=False, idx=None):

  info = {}
  for axis in DIRS:
    info[axis] = {'files': [], 'results': []}
    for figwidth in FIGWIDTHS:
      if DEBUG_SCRIPT:
        print(f"Running visual test with axis='{axis}' and figwidth={figwidth}in")

      files, results = _run_all(axis=axis, figwidth=figwidth, idx=idx, debug=debug)
      info[axis]['files'] += files
      info[axis]['results'] += results

    #files[axis] = sorted(files[axis])

  if idx is None:
    _readmes(info, debug=debug)


def _run_all(axis='x', figwidth=6.4, idx=None, short=False, debug=False):

  import json
  test_file = os.path.join(_script_dir(), 'visual_test.json')
  with open(test_file, 'r') as file:
    tests_manual = json.load(file)

  tests_generated = util.generate_main_tests()

  files = []
  results = []
  tidx = 1
  for entries in [tests_manual, tests_generated]:
    for test in entries:
      if idx is not None and idx != tidx:
        tidx += 1
        continue

      dt_str_o = test['start']
      dt_str_f = test['stop']

      # Keep only 
      kwargs = {k: v for k, v in test.items() if not k.startswith('_') and k not in ('start', 'stop')}

      if DEBUG_SCRIPT:
        print(f"{tidx}. delta_t={test['_delta_t']} | start={dt_str_o} | stop={dt_str_f} | kwargs={kwargs}")

      result = _plot(dt_str_o, dt_str_f, axis=axis, figwidth=figwidth, min_font_size=None, min_gap_warn=True, debug=debug, **kwargs)
      results.append(result)

      file = _savefig(dt_str_o, dt_str_f, axis, figwidth, files, debug=debug)
      files.append(file)

      if short or tidx >= N_MAX:
        break

      tidx += 1

  return files, results


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
      figsize=(figwidth, 3)
      hspace = 1.0
    else:
      figsize=(3, figwidth)
      hspace = 0.1

    fig, axes = matplotlib.pyplot.subplots(3, figsize=figsize)
    matplotlib.pyplot.subplots_adjust(hspace=hspace)
    for ax in axes:
      ax.grid()
      ax.set_ylabel('y') if axis == 'x' else ax.set_xlabel('x')
      if False:
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
      xt = 0.0
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
        if key in ('debug', 'min_gap_warn', 'min_font_size'):
          continue
        text += f'\n{key}={value}'

    ax.text(xt, yt, text, ha='center', va='center', bbox=bbox, fontsize=9)


  fig, axes = _axes(axis, figwidth)

  dt1 = util.parse_ds(ds1)
  dt2 = util.parse_ds(ds2)
  if axis == 'x':
    x = [dt1, dt2]
    y = [-1, 1]
  else:
    x = [-1, 1]
    y = [dt1, dt2]

  from matplotlib import dates as mdates

  axes[0].plot(x, y, '*')
  _set_label(axes[0], axis, x, y, 'matplotlib')


  locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
  # https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter
  formatter = mdates.ConciseDateFormatter(locator)
  axes[1].xaxis.set_major_locator(locator)
  axes[1].xaxis.set_major_formatter(formatter)
  axes[1].plot(x, y, '*')
  _set_label(axes[1], axis, x, y, 'matplotlib+AutoDateLocator/ConciseDateFormatter')


  axes[2].plot(x, y, '*')
  _set_label(axes[2], axis, x, y, 'datetick', datetick_kwargs=kwargs)

  result = datetick.datetick(axis, axes=axes[2], **kwargs)
  _set_title(axes[0], axis, result['delta_t'])

  return result


def _readmes(results, debug=False):

  def _image_subsection(results, latest_dir, base, axis):
    image_links = []

    files = results['files']
    results = results['results']

    for idx, file in enumerate(files):
      note = f"{idx+1}\\."
      if results[idx]['font_size_change'] != 0:
        note += f" (font size change: {results[idx]['font_size_change']:.1f} pt)"
      if results[idx]['rule_idx_change'] != 0:
        note += f" (rule change: {results[idx]['rule_idx_change']})"
      if len(note) > 0:
        note = f"\n{note}\n\n"

      # Copy file to test/visual_tests/latest for linking in README
      latest_file = os.path.join(latest_dir, os.path.basename(file))
      with open(file, 'rb') as src, open(latest_file, 'wb') as dst:
        dst.write(src.read())

      # Make path relative to README dir
      file = os.path.relpath(latest_file, os.path.dirname(readme))
      image_links.append(f'{note}![{file}]({base}{file})')

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
  mpl = f"Matplotlib-{matplotlib.pyplot.matplotlib.__version__}"
  py = f"Python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  image_lines = []
  lines.append(f"\n\n<code>{py}/{mpl}</code>\n\n")

  base = "https://raw.githubusercontent.com/rweigel/datetick/main/"
  latest_dir = os.path.join(_script_dir(), 'visual_test', 'latest')
  os.makedirs(latest_dir, exist_ok=True)

  for axis in results.keys():
    image_lines.append(_image_subsection(results[axis], latest_dir, base, axis))

  n_images = sum(len(results[axis]['files']) for axis in results.keys())

  combined_lines = lines + image_lines
  if DEBUG_SCRIPT:
    print(f"\nUpdating {readme} with {n_images} images")
  with open(readme, 'w') as file:
    file.writelines(combined_lines)

  # Create README.rel.md with base replaced with relative path for local viewing
  readme_rel = os.path.join(os.path.dirname(readme), 'README.rel.md')
  if DEBUG_SCRIPT:
    print(f"Writing {readme_rel} with URL replaced by relative path")
  with open(readme_rel, 'w') as file:
    file.writelines(line.replace(base, "") for line in combined_lines)

  readme = os.path.join(_out_dir(axis), 'README.md')
  if DEBUG_SCRIPT:
    print(f"Writing {readme} in image subdirectory.")
  with open(readme, 'w') as file:
    file.writelines("\n" + "\n\n".join(image_lines))


def _supported_figfmts():
  from matplotlib.backend_bases import FigureCanvasBase
  return tuple(sorted(FigureCanvasBase.get_supported_filetypes().keys()))

def _savefig(ds1, ds2, axis, figwidth, files, debug=False):
  ds1 = ds1.replace(":","").replace("-","").replace("T","").replace("Z","")
  ds2 = ds2.replace(":","").replace("-","").replace("T","").replace("Z","")

  base = f'{_out_dir(axis)}/{ds1}-{ds2}-{figwidth}in'
  file = f'{base}_v1.{FIGFMT}'
  if file in files:
    v = 2
    while file in files:
      file = f'{base}_v{v}.{FIGFMT}'
      v += 1

  if DEBUG_SCRIPT:
    print("  Writing", file)
  dirname = os.path.dirname(file)
  if not os.path.exists(dirname):
    os.makedirs(dirname, exist_ok=True)
  kwargs = {'bbox_inches': 'tight'}

  rc = {}
  if FIGFMT == 'png':
    kwargs['dpi'] = 220
  elif FIGFMT == 'svg':
    # Don't convert text to paths in SVG to keep it searchable and selectable
    kwargs['metadata'] = {"Date": None}  # Remove creation date for testing
    rc = {'svg.fonttype': 'none', 'svg.hashsalt': '67'}

  with matplotlib.pyplot.rc_context(rc):
    matplotlib.pyplot.savefig(file, **kwargs)

  if SHOW_FIG:
    matplotlib.pyplot.show()
  matplotlib.pyplot.close()

  if OPEN_FIG:
    _open_figure(file)

  return file


def _out_dir(axis):
  mpl = f"mpl-{matplotlib.pyplot.matplotlib.__version__}"
  py = f"python-{os.sys.version_info.major}.{os.sys.version_info.minor}"
  return os.path.join(_script_dir(), 'visual_test', py, mpl, axis)


def _script_dir():
  return os.path.dirname(os.path.realpath(__file__))


def _open_figure(path):
  import subprocess
  from PIL import Image, ImageTk, UnidentifiedImageError

  def _show_with_tk(image):
    import tkinter as tk

    root = tk.Tk()
    root.title(os.path.basename(path))

    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo, borderwidth=0)
    label.image = photo
    label.pack()

    root.mainloop()

  try:
    with Image.open(path) as image:
      image.load()
      _show_with_tk(image)
    return
  except (UnidentifiedImageError, OSError, RuntimeError, ImportError):
    pass

  if os.sys.platform == 'darwin':
    command = ['open', '-W', path]
  elif os.name == 'nt':
    os.startfile(path)
    return
  else:
    command = ['xdg-open', path]
  subprocess.run(command, check=False)


def _use_default_interactive_backend():
  try:
    matplotlib.pyplot.switch_backend(matplotlib.rcParamsOrig.get('backend'))
  except Exception as exc:
    raise RuntimeError(f"Could not switch to the default interactive backend: {exc}") from exc


def cli():
  import ast
  import argparse
  global DIRS, FIGWIDTHS, FIGFMT, OPEN_FIG, SHOW_FIG, DEBUG_SCRIPT, N_MAX

  def parse_figwidths(value):
    return [float(part) for part in value.split(',') if part]

  def parse_dirs(value):
    dirs = [part for part in value.split(',') if part]
    if not all(part in ('x', 'y') for part in dirs):
      raise argparse.ArgumentTypeError("dirs must be a comma-separated list containing only 'x' and/or 'y'")
    return dirs

  def parse_figfmt(value):
    figfmt = value.lower()
    if figfmt not in _supported_figfmts():
      supported = ', '.join(_supported_figfmts())
      raise argparse.ArgumentTypeError(f"unsupported figfmt {value!r}; choose from: {supported}")
    return figfmt

  def parse_plot_kwargs(unknown_args):
    kwargs = {}
    idx = 0
    while idx < len(unknown_args):
      arg = unknown_args[idx]
      if not arg.startswith('--'):
        raise argparse.ArgumentTypeError(f'unrecognized argument: {arg}')

      key = arg[2:].replace('-', '_')
      if idx + 1 >= len(unknown_args) or unknown_args[idx + 1].startswith('--'):
        kwargs[key] = True
        idx += 1
        continue

      raw_value = unknown_args[idx + 1]
      lowered = raw_value.lower()
      if lowered == 'true':
        value = True
      elif lowered == 'false':
        value = False
      elif lowered == 'none':
        value = None
      else:
        try:
          value = ast.literal_eval(raw_value)
        except (ValueError, SyntaxError):
          value = raw_value

      kwargs[key] = value
      idx += 2

    return kwargs

  parser = argparse.ArgumentParser(
    usage=(
      'visual_test.py [--idx IDX] [--n-max N] [--debug] [--debug-script {0,1}] '
      '[--figwidths W1,W2] [--dirs x[,y]] [--figfmt FORMAT] [--open] [--show]\n\n'
      '       visual_test.py short [--debug] [--debug-script {0,1}]\n\n'
      '       visual_test.py unit [--start START] [--stop STOP] [--axis {x,y}] '
      '[--figwidth W] [--figfmt FORMAT] [--open] [--show] [--debug] [--debug-script {0,1}] [--PLOT-KWARGS ...]'
    ),
    description=(
      'Run datetick visual tests.\n\n'
      'Modes:\n'
      '  default  Run the full visual test driver.\n'
      '  short    Run only the short smoke-test path.\n'
      '  unit     Run a single unit-style plot with explicit start/stop values.'
    ),
    formatter_class=argparse.RawTextHelpFormatter,
    epilog=(
      'Mode-specific arguments:\n'
      '  default:\n'
      '    --idx IDX\n'
      '    --n-max N\n'
      '    --debug\n'
      '    --debug-script {0,1}\n'
      '    --figwidths W1,W2\n'
      '    --dirs x[,y]\n'
      '    --figfmt FORMAT\n'
      '    --open\n\n'
      '  short:\n'
      '    --debug\n'
      '    --debug-script {0,1}\n\n'
      '  unit:\n'
      '    --start START\n'
      '    --stop STOP\n'
      '    --axis {x,y}\n'
      '    --figwidth W\n'
      '    --figfmt FORMAT\n'
      '    --open\n'
      '    --show\n'
      '    --debug\n'
      '    --debug-script {0,1}\n'
      f'    supported formats: {", ".join(_supported_figfmts())}\n'
      '    extra datetick() kwargs as --name value pairs, for example: --adjust-range False --rule-idx 2'
    ),
  )
  parser.add_argument('command', nargs='?', choices=('short', 'unit'), help='Optional command mode: short or unit.')
  parser.add_argument('--idx', type=int, help='Run only the test case with the given index (1-based).')
  parser.add_argument('--n-max', type=int, help='Maximum number of cases to run.')
  parser.add_argument('--debug', action='store_true', help='Enable datetick debug output.')
  parser.add_argument('--debug-script', action='store_true', help='Enable or disable script debug output.')
  parser.add_argument('--figwidths', type=parse_figwidths, help='Comma-separated figure widths in inches.')
  parser.add_argument('--figfmt', type=parse_figfmt, help='Image format for saved output.')
  parser.add_argument('--open', action='store_true', help='Open each saved figure after writing it.')
  parser.add_argument('--show', action='store_true', help='Use the default interactive backend and show each plot window.')
  parser.add_argument('--dirs', type=parse_dirs, help="Comma-separated plot axes, e.g. 'x' or 'x,y'.")
  parser.add_argument('--start', help='Unit mode start datetime string.')
  parser.add_argument('--stop', help='Unit mode stop datetime string.')
  parser.add_argument('--axis', choices=('x', 'y'), help='Unit mode plot axis.')
  parser.add_argument('--figwidth', type=float, help='Unit mode figure width in inches.')

  args, unknown_args = parser.parse_known_args()
  legacy_commands = [arg for arg in unknown_args if arg in ('--short', '--unit')]
  if legacy_commands:
    parser.error(f"use positional command names instead of flags: {', '.join(legacy_commands)}")
  plot_kwargs = parse_plot_kwargs(unknown_args)

  if args.n_max is not None:
    N_MAX = args.n_max
  if args.debug_script is not None:
    DEBUG_SCRIPT = bool(args.debug_script)
  if args.figwidths is not None:
    FIGWIDTHS = args.figwidths
  if args.figfmt is not None:
    FIGFMT = args.figfmt
  OPEN_FIG = args.open
  SHOW_FIG = args.show
  if args.dirs is not None:
    DIRS = args.dirs

  if OPEN_FIG and SHOW_FIG:
    parser.error("--open and --show cannot be used together")
  if SHOW_FIG:
    _use_default_interactive_backend()

  command = args.command

  if command == 'short':
    invalid_short_args = []
    if args.idx is not None:
      invalid_short_args.append('--idx')
    if args.n_max is not None:
      invalid_short_args.append('--n-max')
    if args.figwidths is not None:
      invalid_short_args.append('--figwidths')
    if args.dirs is not None:
      invalid_short_args.append('--dirs')
    if args.figfmt is not None:
      invalid_short_args.append('--figfmt')
    if args.open:
      invalid_short_args.append('--open')
    if args.show:
      invalid_short_args.append('--show')
    if args.start is not None:
      invalid_short_args.append('--start')
    if args.stop is not None:
      invalid_short_args.append('--stop')
    if args.axis is not None:
      invalid_short_args.append('--axis')
    if args.figwidth is not None:
      invalid_short_args.append('--figwidth')
    if plot_kwargs:
      invalid_short_args.extend(f'--{key.replace("_", "-")}' for key in sorted(plot_kwargs))
    if invalid_short_args:
      parser.error(f"short command only accepts --debug and --debug-script; invalid: {', '.join(invalid_short_args)}")
    test_one(debug=args.debug)
  elif command == 'unit':
    invalid_unit_args = []
    if args.idx is not None:
      invalid_unit_args.append('--idx')
    if args.n_max is not None:
      invalid_unit_args.append('--n-max')
    if args.figwidths is not None:
      invalid_unit_args.append('--figwidths')
    if args.dirs is not None:
      invalid_unit_args.append('--dirs')
    if invalid_unit_args:
      parser.error(f"unit command only accepts unit-mode options; invalid: {', '.join(invalid_unit_args)}")
    _unit(
      start=args.start,
      stop=args.stop,
      axis=args.axis,
      figwidth=args.figwidth,
      debug=args.debug,
      **plot_kwargs,
    )
  elif args.idx is not None:
    test_all(debug=args.debug, idx=args.idx)
  else:
    test_all(debug=args.debug)


def _unit(start=None, stop=None, axis='x', figwidth=22.5, debug=True, **kwargs):
  ds1 = '2001-01-01T23:59:56.85Z' if start is None else start
  ds2 = '2001-01-02T00:00:00.35Z' if stop is None else stop
  axis = 'x' if axis is None else axis
  figwidth = 22.5 if figwidth is None else figwidth
  _plot(ds1, ds2, axis=axis, figwidth=figwidth, debug=debug, **kwargs)
  outfile = f'unit.{FIGFMT}'
  print("Writing", outfile)
  savefig_kwargs = {'bbox_inches': 'tight'}
  if FIGFMT == 'png':
    savefig_kwargs['dpi'] = 300
  elif FIGFMT == 'svg':
    savefig_kwargs['metadata'] = {"Date": None}
  with matplotlib.pyplot.rc_context({'svg.fonttype': 'none', 'svg.hashsalt': '67'} if FIGFMT == 'svg' else {}):
    matplotlib.pyplot.savefig(outfile, **savefig_kwargs)
  if SHOW_FIG:
    matplotlib.pyplot.show()
  matplotlib.pyplot.close()
  if OPEN_FIG:
    _open_figure(outfile)

if __name__ == '__main__':
  cli()
