import numpy as np

def print_matrix(matrix: list[int][int]):
    for i in range(len(matrix)):
        print()
        for j in range(len(matrix)):
            print(f"|{matrix[i][j]:g}", sep = "  ", end = "|")

def init_matrix() -> list[int][int]:
    n = int(input(("Введите кол-во строк ")))
    m = int(input(("Введите кол-во столбцов ")))
    matrix = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            matrix[i][j] = int(input(f"Введите значение для [{i}] [{j}] "))
    
    return matrix

def get_matrix_sum(matrix1: list[int][int], matrix2: list[int][int]) -> list[int][int]:
    answer = np.zeros((len(matrix1), len(matrix1[0])))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            answer[i][j] = matrix1[i][j] + matrix2[i][j]

    return answer;

def get_matrix_diff(matrix1: list[int][int], matrix2: list[int][int]) -> list[int][int]:
    answer = np.zeros((len(matrix1), len(matrix1[0])))
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
             answer[i][j] = matrix1[i][j] - matrix1[i][j]
    
    return answer;

def get_matrix_mult(matrix1: list[int][int], matrix2: list[int][int]) -> list[int][int]:
    answer = np.zeros((len(matrix1), len(matrix2[0])))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                answer[i][j] = matrix1[i][k] * matrix2[k][j]

    return answer

def check_status():
    print("Какую операцию хотите совершить?", "1 - Сумма", "2 - Вычитание", "3 - Умножение", sep = "\n", end = "\n")
    status = int(input())
    matrix1 = init_matrix()
    matrix2 = init_matrix()
    match status:
        case 1:
            print_matrix(get_matrix_sum(matrix1, matrix2))
        case 2:
            print_matrix(get_matrix_diff(matrix1, matrix2))
        case 3:
            print_matrix(get_matrix_mult(matrix1, matrix2))
        case _:
            print("Неизвестный статус")