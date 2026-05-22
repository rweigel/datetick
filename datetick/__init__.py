from .datetick import datetick
from . import rules
from . import util

__all__ = ['datetick', 'util', 'rules', '__version__']


try:
    from importlib.metadata import version
    __version__ = version('datetick')
except:
    __version__ = 'unknown'
