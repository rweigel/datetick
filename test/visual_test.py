# Create plots with varying time ranges.

import os
import dateutil.parser
import matplotlib.pyplot as plt

from datetick import datetick

try:
  import yaml
except ImportError:
  print("PyYAML is required to run this test. Please install it with 'pip install pyyaml'")
  exit()

try:
  import pytest
except ImportError:
  print("pytest is required to run this test. Please install it with 'pip install pytest'")
  exit()

def plot(ds1, ds2, dir, **kwargs):
  if dir == 'x':
    figsize=(8, 2)
    hspace = 1.0
  else:
    figsize=(2, 8)
    hspace = 0.1

  _, axes = plt.subplots(2, figsize=figsize)
  plt.subplots_adjust(hspace=hspace)
  for axis in axes:
    axis.grid()
    if dir == 'x':
      axis.spines[['top', 'right', 'left']].set_visible(False)
      axis.yaxis.set_visible(False)
    else:
      axis.spines[['top', 'right']].set_visible(False)

  bbox = {
          'boxstyle': 'round,pad=0.3',
          'facecolor': 'white',
          'edgecolor': 'gray',
          'alpha': 0.8
  }
  text_matplotlib = 'matplotlib'
  text_datetick = 'datetick'
  if kwargs:
    bbox['facecolor'] = 'lightblue'
    for key, value in kwargs.items():
      if key == 'debug':
        continue
      text_datetick += f'\n{key}={value}'

  dt1 = dateutil.parser.parse(ds1)
  dt2 = dateutil.parser.parse(ds2)
  if dir == 'x':
    x = [dt1, dt2]
    y = [0.0,0.0]
    yt = 0.0
    xt = x[0] + (x[1] - x[0])/2
  else:
    x = [0.0, 1.0]
    y = [dt1, dt2]
    xt = 0.5
    yt = y[0] + (y[1] - y[0])/2

  if dir == 'x':
    newline = ''
    space = ''
  else:
    newline = '\n'
    space = '   '
  axes[0].set_title(ds1 + f' - {newline}' + ds2 + space, fontsize=10, fontfamily='monospace')
  axes[0].plot(x, y, '*')
  axes[0].text(xt, yt, text_matplotlib, ha='center', bbox=bbox)

  axes[1].plot(x, y, '*')
  axes[1].text(xt, yt, text_datetick, ha='center', bbox=bbox)
  datetick(dir, axes=axes[1], **kwargs)


def _savefig(ds1, ds2, dir, files, debug=False):
  ds1 = ds1.replace(":","").replace("-","").replace("T","").replace("Z","")
  ds2 = ds2.replace(":","").replace("-","").replace("T","").replace("Z","")

  ext = 'png'
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

  plt.savefig(file, bbox_inches='tight', dpi=300)
  plt.close()

  return file


def _append_to_readme(files, dir, debug=False):

  readme = 'README.md' # Repo README
  readme = os.path.join(_script_dir(), "..", readme)

  with open(readme, 'r+') as file:
    lines = file.readlines()

  index = next(i for i, line in enumerate(lines) if "Comparison to default Matplotlib" in line)
  del lines[index+1:]

  image_links = []
  for file in files:
    # Make path relative to README
    base = "https://raw.githubusercontent.com/rweigel/datetick/main/"
    file = os.path.relpath(file, os.path.dirname(readme))
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


@pytest.mark.short
def test_plot_short(debug=False):
  test_plot(short=True, debug=debug)


def test_plot(short=False, debug=False):
  test_file = os.path.join(_script_dir(), 'visual_test.yaml')
  with open(test_file, 'r') as file:
    tests = yaml.safe_load(file)

  dir = 'x'
  files = []
  for test_cat in ['kwargs', 'main']:
    for test in tests[test_cat]:
      kwargs = test[2] if len(test) > 2 else {}
      dt_str_o = test[0]
      dt_str_f = test[1]
      plot(dt_str_o, dt_str_f, dir=dir, **kwargs)
      file = _savefig(dt_str_o, dt_str_f, dir, files)
      files.append(file)
      if short:
        break

  if not short:
    _append_to_readme(files, dir, debug=debug)
    _create_subdir_readme(files, dir, debug=debug)


if __name__ == '__main__':
  if False:
    dir = 'x'
    ds1 = '2001-02-12T00:00:00Z'
    ds2 = '2002-01-31T00:00:00Z'
    file = plot(ds1, ds2, dir, debug=True)
    plt.savefig('a.png', bbox_inches='tight', dpi=300)
    plt.close()
    exit()

  #test_plot(short=True)
  test_plot(debug=True)
