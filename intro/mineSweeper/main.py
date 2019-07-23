def getNeighboors(matrix: list, i: int, j: int) -> list:
    neighboring_cells = []
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if ([k, l] != [0, 0]) and (i+k >= 0) and (i+k < len(matrix)) and (j+l >= 0) and (j+l < len(matrix[0])):
                neighboring_cells.append(matrix[i+k][j+l])
    return neighboring_cells
    
def minesweeper(matrix: list) -> list:
    mines_matrix = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            neighboring_cells = getNeighboors(matrix, i, j)
            count = 0
            for cell in neighboring_cells:
                count += cell
            line.append(count)
        mines_matrix.append(line)
    return mines_matrix