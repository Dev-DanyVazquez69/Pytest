from diagonal_sum import DiagonalSum
import pytest



diagonal_sum = DiagonalSum()

element_max_value = 100
element_min_value = -99

matrix_max_size = 1000
matrix_min_size = 2

@pytest.fixture
def input_matrix():
    matrix = diagonal_sum.matrix
    return matrix


def test_element_type(input_matrix):
    matrix = input_matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert isinstance(matrix[i][j],int), 'Elementos devem ser do tipo inteiro'


def test_elements_lower_limit(input_matrix):
    matrix = input_matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert matrix[i][j] >  element_min_value, f'Elemento de valor {matrix[i][j]} é inferior ao limite de {element_min_value} estabelecido'

def test_elements_upper_limit(input_matrix):
    matrix = input_matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            assert matrix[i][j] <= element_max_value, f'Elemento de valor {matrix[i][j]} é superior ao limite de {element_max_value} estabelecido'


def test_column_size_upper_limit(input_matrix):
    matrix = input_matrix
    for row in matrix:
        assert len(row) <= matrix_max_size, f'Matriz de número de colunas superior ao limite de {matrix_max_size} estabelecido'

def test_row_size_upper_limit(input_matrix):
    matrix = input_matrix
    row_n = len(matrix)
    assert row_n <= matrix_max_size, f'Matriz de número de linhas superior ao limite de {matrix_max_size} estabelecido'

def test_column_size_lower_limit(input_matrix):
    matrix = input_matrix
    for row in matrix:
        colums_n = len(row)
        assert colums_n >= matrix_min_size, f'Matriz de número de colunas inferior ao limite de {matrix_max_size} estabelecido'

def test_row_size_lower_limit(input_matrix):
    matrix = input_matrix
    row_n = len(matrix)
    assert row_n >= matrix_min_size, f'Matriz de número de linhas inferior ao limite de {matrix_max_size} estabelecido'


# Testa se todas as linhas possuem o mesmo número de colunas 
def test_size_rows(input_matrix):
    matrix = input_matrix
    size = len(matrix[0])
    for row in matrix:
        assert len(row) == size

# Testa se a matriz possui o mesmo número de linhas e colunas
def test_matrix_is_square(input_matrix):
    matrix = input_matrix
    n_rows = len(matrix)
    for row in matrix:
        assert len(row) == n_rows


@pytest.fixture
def input_difference():
    difference = diagonal_sum.diagonal_abs_difference()
    return difference


def test_diagonal_is_positive(input_difference):
    assert input_difference >= 0

    

