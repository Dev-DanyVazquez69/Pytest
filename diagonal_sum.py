import pytest

class DiagonalSum():

    matrix =    [[-0,-20,50],
                [4,-50,-6],
                [-10,8,99]]

    matrix_n = len(matrix[1]) 

    def __init__(self):
        self.matrix = DiagonalSum.matrix
        

        self.left_diagonal_sum = self.get_left_diagonal()
        self.right_diagonal_sum = self.get_right_diagonal()

    def get_left_diagonal(self):
        left_diagonal_sum = 0
        for i in range(DiagonalSum.matrix_n):
            for j in range(DiagonalSum.matrix_n):
                if i == j:
                    left_diagonal_sum = left_diagonal_sum + DiagonalSum.matrix[i][j]
        return left_diagonal_sum


    def get_right_diagonal(self):
        right_diagonal_sum = 0
        for i in range(DiagonalSum.matrix_n):
            for j in range(DiagonalSum.matrix_n):
                if i + j == DiagonalSum.matrix_n - 1:
                    right_diagonal_sum = right_diagonal_sum + DiagonalSum.matrix[i][j]
        return right_diagonal_sum


    def diagonal_abs_difference(self):



        difference = self.left_diagonal_sum  - self.right_diagonal_sum
        abs_difference = abs(difference)

        print(f'Left: {self.left_diagonal_sum} Right: {self.right_diagonal_sum}')
        print(F"Difference: {difference}, Absolute difference: {abs_difference}")
        return abs_difference




sum = DiagonalSum()
sum.diagonal_abs_difference()
pytest.main(['--verbose'])