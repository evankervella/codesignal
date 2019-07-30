def differentSquares(matrix: list) -> int:
    h_square = 2
    l_square = 2
    x = len(matrix)
    y = len(matrix[0])
    squares = []
    for i in range(x-h_square+1):
        tmp_matrix = matrix[i:i+h_square]
        for j in range(y-l_square+1):
            square = [line[j:j+l_square] for line in tmp_matrix]
            if square not in squares:
                squares.append(square)
    return len(squares)