import helper_functions
import numpy as np
import re


def findhorizontally(lines: list[str]) -> int:
    count: int = 0
    for line in lines:
        forward: int = line.count("XMAS")
        backward: int = line.count("SAMX")
        count += forward + backward
    return count


def findvertically(lines: list[str]) -> int:
    matrix = np.array([np.array(list(xi)) for xi in lines])
    matrix = matrix.transpose()
    transformed_list: list = []
    line: np.ndarray
    for line in matrix:
        string = ''.join(line.tolist())
        transformed_list.append(string)
    return findhorizontally(transformed_list)


def finddiagonal(lines: list[str]) -> int:
    matrix = np.array([np.array(list(xi)) for xi in lines])
    matrix2 = np.array([np.array(list(xi)) for xi in lines])
    matrix2 = np.fliplr(matrix2) #mirros the matrix, so that the main diagonal is the opposite diagonal and vice versa
    list_diagonals = []
    list_otherdiagonals = []
    for i in range(-matrix.shape[1], matrix.shape[1]):
        list_diagonals.append(''.join(matrix.diagonal(offset=i, axis1=0, axis2=1).tolist()))
    for i in range(-matrix2.shape[1], matrix2.shape[1]):
        list_otherdiagonals.append(''.join(matrix2.diagonal(offset=i, axis1=0, axis2=1).tolist()))
    return findhorizontally(list_diagonals) + findhorizontally(list_otherdiagonals)


def findSAMX(lines: list[str]) -> int:
    matrix = np.array([np.array(list(xi)) for xi in lines])
    matrix2 = np.array([np.array(list(xi)) for xi in lines])
    matrix2 = np.fliplr(matrix2)  # mirros the matrix, so that the main diagonal is the opposite diagonal and vice versa
    list_diagonals = []
    list_otherdiagonals = []
    for i in range(-matrix.shape[1], matrix.shape[1]):
        list_diagonals.append(''.join(matrix.diagonal(offset=i, axis1=0, axis2=1).tolist()))
    for i in range(-matrix2.shape[1], matrix2.shape[1]):
        list_otherdiagonals.append(''.join(matrix2.diagonal(offset=i, axis1=0, axis2=1).tolist()))

    matches_diagonals = []
    matches_other_diagonals = []

    for i in range(len(list_diagonals)):
        matches_diagonals.append([m.start() for m in re.finditer(r'MAS|SAM', list_diagonals[i])])
    for i in range(len(list_otherdiagonals)):
        matches_other_diagonals.append([m.start() for m in re.finditer(r'MAS|SAM', list_otherdiagonals[i])])
    count = 0
    for i in range(len(matches_diagonals)):
        if matches_diagonals[i].count == 0:
            continue
        for match in matches_diagonals[i]:
            if matches_other_diagonals[i].count(140-match + 2) > 0:
                count += 1
    return count

def find_cross(lines: list[str]) -> int:
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'A' and 0 < i < len(lines)-1 and 0 < j < len(lines[i])-1:
                if (lines[i + 1][j + 1] == 'S' and lines[i - 1][j - 1] == 'M') or (lines[i + 1][j + 1] == 'M' and lines[i - 1][j - 1] == 'S'):
                    if (lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M') or (
                                lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S'):
                        count += 1
    return count



def solve():
    input_text: str = helper_functions.read_in_file(4)
    lines = input_text.splitlines()
    #part 1:
    #count = findhorizontally(lines) + findvertically(lines) + finddiagonal(lines)

    #part 2:
    print(find_cross(lines))

