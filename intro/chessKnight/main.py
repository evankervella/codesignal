def isMoveOkay(move: list) -> bool:
    l_dim = 8
    h_dim = 8
    x, y = move[0], move[1]
    if x < 0 or y < 0 or x > l_dim-1 or y > h_dim-1:
        return False
    return True

def chessKnight(cell: str) -> int:
    x = ord(cell[0])-ord('a')
    y = int(cell[1])-1
    potential_moves = []
    for i in [-2,-1,1,2]:
        for j in [-2,-1,1,2]:
            if abs(i) != abs(j):
                potential_moves.append([x+i, y+j])
    count_moves = 0
    for move in potential_moves:
        if isMoveOkay(move):
            count_moves += 1
    return count_moves