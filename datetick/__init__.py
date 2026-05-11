from .datetick import datetick
from . import rules
from . import util

__all__ = ['datetick', 'util', 'rules', '__version__']

from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version('datetick')
except PackageNotFoundError:
    __version__ = 'unknown'