import numpy as np

def checkSubgrids(grid: list) -> bool:
    size_subgrid = 3
    for i in range(size_subgrid):
        tmp_subgrid = grid[np.ix_([(3*i)+0, (3*i)+1, (3*i)+2], [(3*i)+0, (3*i)+1, (3*i)+2])]
        for num in range(1, 10):
            if num not in [item for list_ in tmp_subgrid for item in list_]:
                return False
    return True
    
def checkColumns(grid: list) -> bool:
    for row in grid.T:
        for num in range(1, 10):
            if num not in row:
                return False
    return True
    
def checkRows(grid: list) -> bool:
    for row in grid:
        for num in range(1, 10):
            if num not in row:
                return False
    return True

def sudoku(grid: list) -> bool:
    grid = np.array(grid)
    if not (checkSubgrids(grid) and checkColumns(grid) and checkRows(grid)):
        return False
    return True