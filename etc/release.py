"""
Create GitHub and PyPi releases with the same version number as the datetick package.
This script should be run after updating the version number in pyproject.toml
and before pushing to GitHub.
"""

import os
import sys
import subprocess
from importlib.metadata import version as pkg_version, PackageNotFoundError

def main():
  try:
    version = pkg_version('datetick')
  except PackageNotFoundError:
    print("datetick is not installed. Run: pip install -e .")
    sys.exit(1)

  print(f"Creating release {version} on GitHub and PyPi")

  # Create GitHub release
  subprocess.run(['gh', 'release', 'create', version, '-t', version, '-n', f'Release {version}'], check=True)

  # Create PyPi release
  subprocess.run(['python', '-m', 'build'], check=True)
  config_file = os.path.expanduser('~/git/admin/etc/pypirc')
  subprocess.run(['twine', 'upload', '--config-file', config_file, 'dist/*'], check=True)