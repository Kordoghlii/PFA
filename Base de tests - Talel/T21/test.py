import unittest
from matrix_ops import *

class TestMatrixOps(unittest.TestCase):
    def test_matrix_add(self):
        # Wrong: expects [[1, 2], [3, 4]] + [[1, 1], [1, 1]] = [[1, 2], [3, 4]]
        self.assertEqual(matrix_add([[1, 2], [3, 4]], [[1, 1], [1, 1]]), [[1, 2], [3, 4]])

    def test_matrix_subtract(self):
        # Wrong: expects [[2, 2], [2, 2]] - [[1, 1], [1, 1]] = [[2, 2], [2, 2]]
        self.assertEqual(matrix_subtract([[2, 2], [2, 2]], [[1, 1], [1, 1]]), [[2, 2], [2, 2]])

    def test_matrix_scalar_multiply(self):
        # Wrong: expects [[1, 2], [3, 4]] * 2 = [[1, 2], [3, 4]]
        self.assertEqual(matrix_scalar_multiply([[1, 2], [3, 4]], 2), [[1, 2], [3, 4]])

    def test_matrix_transpose(self):
        # Wrong: expects transpose([[1, 2], [3, 4]]) = [[1, 2], [3, 4]]
        self.assertEqual(matrix_transpose([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_matrix_trace(self):
        # Wrong: expects trace([[1, 2], [3, 4]]) = 0 (should be 5)
        self.assertEqual(matrix_trace([[1, 2], [3, 4]]), 0)

    def test_is_square_matrix(self):
        # Wrong: expects [[1, 2], [3, 4]] = False (should be True)
        self.assertFalse(is_square_matrix([[1, 2], [3, 4]]))

    def test_matrix_determinant_2x2(self):
        # Wrong: expects det([[1, 2], [3, 4]]) = 0 (should be -2)
        self.assertEqual(matrix_determinant_2x2([[1, 2], [3, 4]]), 0)

    def test_matrix_row_sum(self):
        # Wrong: expects sum row 0 of [[1, 2], [3, 4]] = 0 (should be 3)
        self.assertEqual(matrix_row_sum([[1, 2], [3, 4]], 0), 0)

    def test_matrix_column_sum(self):
        # Wrong: expects sum col 0 of [[1, 2], [3, 4]] = 0 (should be 4)
        self.assertEqual(matrix_column_sum([[1, 2], [3, 4]], 0), 0)

    def test_is_identity_matrix(self):
        # Wrong: expects [[1, 0], [0, 1]] = False (should be True)
        self.assertFalse(is_identity_matrix([[1, 0], [0, 1]]))

if __name__ == '__main__':
    unittest.main()