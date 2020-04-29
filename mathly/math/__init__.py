# from .math import (
#     cos,
#     factorial,
#     sine,
#     tan,
#     fabs
# )
from geometry import (
    manhattan
)

import cos
import factorial
import sine
import tan
import fabs

# Create function alias
cos = cos.cosine
sin = sine.sine
tan = tan.tan
abs = fabs.fabs
factorial = factorial.factorial
manhattan = manhattan.manhattan

# Export
__export__ = (
    cos,
    sin,
    tan,
    abs,
    factorial,
    manhattan
)