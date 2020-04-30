# import error
# try:
# if __package__ is None or __package__ == "":
#     from .shared import *
# else:
# from mathly.shared.version import VERSION
from .shared import *
# except:
    # print("Couldn't import Mathly shared module!")
# try:
from .math import *
# except ImportError:
    # print("Couldn't import Mathly math module!")

__all__ = []
# __all__.extend(M.__export__)

# __version__ = VERSION