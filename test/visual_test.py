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

debug = False

def plot(ds1, ds2, **kwargs):
  _, axes = plt.subplots(2, figsize=(8, 2))
  plt.subplots_adjust(hspace=1.0)
  for axis in axes:
    axis.grid()
    axis.spines[['top', 'right', 'left']].set_visible(False)
    axis.yaxis.set_visible(False)

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
      text_datetick += f'\n{key}={value}'

  dt1 = dateutil.parser.parse(ds1)
  dt2 = dateutil.parser.parse(ds2)
  x = [dt1, dt2]
  xt = x[0] + (x[1] - x[0])/2
  y = [0.0,0.0]

  axes[0].set_title(ds1 + ' - ' + ds2, fontfamily='monospace')
  axes[0].plot(x, y, '*')
  axes[0].text(xt, 0.00, text_matplotlib, ha='center', bbox=bbox)

  axes[1].plot(x, y, '*')
  axes[1].text(xt, 0.00, text_datetick, ha='center', bbox=bbox)
  datetick('x', axes=axes[1], debug=debug, **kwargs)


def _savefig(ds1, ds2, files):
  ds1 = ds1.replace(":","").replace("-","").replace("T","").replace("Z","")
  ds2 = ds2.replace(":","").replace("-","").replace("T","").replace("Z","")

  file = f'{_out_dir()}/{ds1}-{ds2}.png'
  if file in files:
    v = 2
    while file in files:
      file = f'{_out_dir()}/{ds1}-{ds2}_{v}.png'
      v += 1

  if debug:
    print("Writing", file)
  dirname = os.path.dirname(file)
  if not os.path.exists(dirname):
    os.makedirs(dirname, exist_ok=True)

  plt.savefig(file, bbox_inches='tight', dpi=300)
  plt.close()

  return file


def _append_to_readme(files):

  readme = 'README.md' # Repo README
  readme = os.path.join(_script_dir(), "..", readme)

  with open(readme, 'r+') as file:
    lines = file.readlines()

  index = next(i for i, line in enumerate(lines) if "Comparison to default Matplotlib" in line)
  del lines[index+1:]

  image_links = []
  for file in files:
    # Make path relative to README
    base = "https://raw.githubusercontent.com/rweigel/utilrsw/main/"
    file = os.path.relpath(file, os.path.dirname(readme))
    image_links.append(f'![{file}]({base}/{file})')

  lines.append("\n" + "\n\n".join(image_links))

  if debug:
    print(f"Updating {readme} with {len(files)} images")
  with open(readme, 'w') as file:
    file.writelines(lines)


def _create_subdir_readme(files):
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
def test_plot_short():
  test_plot(short=True)


def test_plot(short=False):
  test_file = os.path.join(_script_dir(), 'visual_test.yaml')
  with open(test_file, 'r') as file:
    tests = yaml.safe_load(file)

  files = []
  for test_cat in ['kwargs', 'main']:
    for test in tests[test_cat]:
      kwargs = test[2] if len(test) > 2 else {}
      dt_str_o = test[0]
      dt_str_f = test[1]
      plot(dt_str_o, dt_str_f, **kwargs)
      file = _savefig(dt_str_o, dt_str_f, files)
      files.append(file)
      if short:
        break

  if not short:
    _append_to_readme(files)
    _create_subdir_readme(files)


if __name__ == '__main__':
  if False:
    debug = True
    ds1 = '2001-01-01T00:00:00.0Z'
    ds2 = '2001-01-01T00:00:00.1Z'
    file = plot(ds1, ds2)
    _savefig(ds1, ds2, [file])
    exit()


  #test_plot(short=True)
  test_plot()
