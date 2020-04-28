from .error import MatrixError, MathlyAssertError

__all__ = []

class Matrix:
    """
    Implementation of matrices.
    """
    def __init__(self, matrix):
        super().__init__()
        # self.matrix = [[1, 2, 3], [4, 5, 6]]
        self.matrix = matrix
        self.used = []
        # self.shape = self.get_shape()
        self.__all__ = []
        self.__all__.extend("MatrixDef")
    
    def get_shape(self):
        # TODO(aaronhma): Stabilize this:
        self.__all__.extend("MatrixShape")
        shape = set()
        shape.add(len(self.matrix))
        shape.add(len(self.matrix[0]))
        return shape

    def test_valid_matrix(self) -> bool:
        """
        Returns if matrix is valid.
        """
        self.__all__.extend("ValidateMatrix")
        X, y = self.get_shape()
        check_valid_row = False
        check_valid_column = False
        if X == 2:
            check_valid_row = True
        if y >= 1:
            check_valid_column = True
        if check_valid_column and check_valid_row:
            return True
        else:
            raise MatrixError("Invalid matrix!")
    
    def transform(self):
        self.__all__.extend("TransformMatrix")
        # X, y = self.get_shape()
        try:
            assert(self.test_valid_matrix)
        except:
            raise MathlyAssertError("The matrix is invalid!")
        
        return self.shape
    
    def transpose(self):
        self.__all__.extend("TransposeMatrix")
        X, y = self.get_shape()
        
    
matrix = Matrix([[1, 2, 3], [4, 5, 6]])
T = matrix.transpose()
__all__.extend(matrix.__all__)