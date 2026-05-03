from datetick.datetick import datetick
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('datetick')
except PackageNotFoundError:
    __version__ = 'unknown'