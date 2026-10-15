from unittest.mock import patch

from src.functions import (
    check_status,
    get_matrix_diff,
    get_matrix_mult,
    get_matrix_sum,
    init_matrix,
    print_matrix,
)


def test_get_matrix_sum():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    result = get_matrix_sum(matrix1, matrix2)

    assert result.tolist() == [[6, 8], [10, 12]]


def test_get_matrix_diff():
    matrix1 = [[5, 6], [7, 8]]
    matrix2 = [[1, 2], [3, 4]]

    result = get_matrix_diff(matrix1, matrix2)

    assert result.tolist() == [[4, 4], [4, 4]]


def test_get_matrix_mult():
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    result = get_matrix_mult(matrix1, matrix2)

    assert result.tolist() == [[19, 22], [43, 50]]


def test_init_matrix():
    # Вместо ручного ввода: 2 строки, 2 столбца, затем четыре элемента.
    with patch("builtins.input", side_effect=["2", "2", "1", "2", "3", "4"]):
        result = init_matrix()

    assert result.tolist() == [[1, 2], [3, 4]]


def test_print_matrix(capsys):
    matrix = [[1, 2], [3, 4]]

    print_matrix(matrix)

    # capsys позволяет прочитать то, что функция напечатала.
    output = capsys.readouterr().out
    assert output == "\n|1||2|\n|3||4|"


def test_check_status(capsys):
    # Выбираем сложение и вводим две матрицы 1 x 1: [[5]] и [[2]].
    answers = ["1", "1", "1", "5", "1", "1", "2"]
    with patch("builtins.input", side_effect=answers):
        check_status()

    output = capsys.readouterr().out
    assert "|7|" in output
