__error__ = ["BaseError", "MatrixError", "VectorError"]

class BaseError(Exception):
    pass

class MatrixError(BaseError):
    pass

class VectorError(BaseError):
    pass

class MathlyAssertError(AssertionError):
    pass

class MathlyModuleError(ModuleNotFoundError):
    pass