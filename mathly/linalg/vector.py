from .error import VectorError

__all__ = []

class Vector:
    """
    Implementation of a vector.
    """
    def __init__(self, row, column):
        if (row != 0) and (column != 0):
            self.row = row
            self.column = column
            self.__all__ = []
        else:
            self.row = 0
            self.column = 0
            raise VectorError("Failed to parse vector: No arguments specified!")
        # self.size = [row, column]
    
    def transpose(self):
        if self.row: # Row vector
            # TODO: Transpose to column
            pass
        else:
            # TODO: Transpose to vector
            pass
    
    def add(self):
        pass
    
    def subtract(self, vector2):
        pass

vector = Vector()
__all__.extend(vector.__all__)