# import error
try:
    from .shared import version
except:
    print("Couldn't import Mathly shared module!")
try:
    from .math import *
except ImportError:
    print("Couldn't import Mathly math module!")

__all__ = []
# __all__.extend(M.__export__)

__version__ = version.VERSION