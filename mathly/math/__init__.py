from . import (
    cos,  # Cosine
    factorial,  # Factorial
    sine,  # Sin
    tan,  # Tan
    fabs  # Absolute value
)
from .geometry import (
    manhattan
)

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
