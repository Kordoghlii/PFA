def matrix_add(matrix1, matrix2):
    """Add two matrices element-wise.

    Args:
        matrix1 (list): First matrix (list of lists).
        matrix2 (list): Second matrix (list of lists).

    Returns:
        list: Resulting matrix after addition.
    """
    # Add two matrices element-wise
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_subtract(matrix1, matrix2):
    # Subtract matrix2 from matrix1 element-wise
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_scalar_multiply(matrix, scalar):
    # Multiply matrix by a scalar
    return [[matrix[i][j] * scalar for j in range(len(matrix[0]))] for i in range(len(matrix))]

def matrix_transpose(matrix):
    """Transpose a matrix.

    Args:
        matrix (list): Input matrix (list of lists).

    Returns:
        list: Transposed matrix.
    """
    # Transpose matrix (swap rows and columns)
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_trace(matrix):
    # Calculate trace of a square matrix
    return sum(matrix[i][i] for i in range(len(matrix)))

def is_square_matrix(matrix):
    # Check if matrix is square
    return len(matrix) == len(matrix[0]) if matrix else False

def matrix_determinant_2x2(matrix):
    """Calculate determinant of a 2x2 matrix.

    Args:
        matrix (list): 2x2 matrix (list of lists).

    Returns:
        float: Determinant of the matrix.
    """
    # Calculate determinant of 2x2 matrix
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def matrix_row_sum(matrix, row):
    # Sum elements in a specific row
    return sum(matrix[row])

def matrix_column_sum(matrix, col):
    # Sum elements in a specific column
    return sum(matrix[i][col] for i in range(len(matrix)))

def is_identity_matrix(matrix):
    # Check if matrix is an identity matrix
    if not is_square_matrix(matrix):
        return False
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j and matrix[i][j] != 1:
                return False
            if i != j and matrix[i][j] != 0:
                return False
    return True