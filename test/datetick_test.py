# Create plots with varying time ranges.

import os
import yaml
import dateutil.parser
import matplotlib.pyplot as plt

from datetick import datetick

debug = False

def plot(ds1, ds2, **kwargs):
  _, axes = plt.subplots(2, figsize=(8, 2))
  plt.subplots_adjust(hspace=1.0)

  dt1 = dateutil.parser.parse(ds1)
  dt2 = dateutil.parser.parse(ds2)
  x = [dt1, dt2]
  xt = x[0] + (x[1] - x[0])/2
  y = [0.0,0.0]

  bbox = dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8)

  axes[0].set_title(ds1 + ' - ' + ds2, fontfamily='monospace')
  axes[0].plot(x, y, '*')
  axes[0].text(xt, 0.00, 'matplotlib', ha='center', bbox=bbox)

  text = 'datetick'
  if kwargs:
    bbox['facecolor'] = 'lightblue'
    for key, value in kwargs.items():
      text += f'\n{key}={value}'
  axes[1].plot(x, y, '*')
  axes[1].text(xt, 0.00, text, ha='center', bbox=bbox)
  datetick('x', axes=axes[1], debug=debug, **kwargs)

  for axis in axes:
    axis.grid()
    axis.spines[['top', 'right', 'left']].set_visible(False)
    axis.yaxis.set_visible(False)

  file = _savefig(ds1, ds2)

  return file


def _savefig(ds1, ds2):
  ds1 = ds1.replace(":","").replace("-","").replace("T","").replace("Z","")
  ds2 = ds2.replace(":","").replace("-","").replace("T","").replace("Z","")

  file = f'{_script_dir()}/{_mpl_version()}/{ds1}-{ds2}.svg'
  if file in files:
    v = 2
    while file in files:
      file = f'{_script_dir()}/{_mpl_version()}/{ds1}-{ds2}_{v}.svg'
      v += 1

  print("Writing", file)
  dirname = os.path.dirname(file)
  if not os.path.exists(dirname):
    os.makedirs(dirname, exist_ok=True)

  plt.savefig(file, bbox_inches='tight')
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
    file = os.path.relpath(file, os.path.dirname(readme))
    image_links.append(f'![{file}]({file})')

  lines.append("\n" + "\n\n".join(image_links))

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

  readme = os.path.join(_script_dir(), _mpl_version(), 'README.md')
  print(f"Writing {readme} with {len(files)} images")
  with open(readme, 'w') as file:
    file.writelines("\n" + "\n\n".join(image_links))


def _mpl_version():
  return f"mpl-{plt.matplotlib.__version__}"


def _script_dir():
  return os.path.dirname(os.path.realpath(__file__))


if False:
  plot('2001-01-01T00:00:58Z','2001-01-01T00:01:18Z', adjust_xrange=True)
  #plot('2001-01-01T00:00:00Z','2001-01-02T23:00:00Z', adjust_first_xlabel=True)
  exit()

test_file = os.path.join(_script_dir(), 'datetick_test.yaml')
with open(test_file, 'r') as file:
  tests = yaml.safe_load(file)

files = []
for test in tests['main']:
  kwargs = test[2] if len(test) > 2 else {}
  file = plot(test[0], test[1], **kwargs)
  files.append(file)

_append_to_readme(files)
_create_subdir_readme(files)