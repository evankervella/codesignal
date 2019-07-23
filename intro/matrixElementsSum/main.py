def matrixElementsSum(matrix: list) -> int:
    tmp_matrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if tmp_matrix[i][j] == 0:
                for k in range(i,len(matrix)):
                    tmp_matrix[k][j] = 0
    return sum([sum(elt) for elt in tmp_matrix])