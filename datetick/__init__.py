from .datetick import datetick
from . import util

__all__ = ['datetick', 'util', '__version__']

from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version('datetick')
except PackageNotFoundError:
    __version__ = 'unknown'