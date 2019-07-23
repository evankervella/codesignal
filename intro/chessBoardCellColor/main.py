def chessBoardCellColor(cell1: str, cell2: str) -> bool:
    letter1 = cell1[0]
    number1 = int(cell1[1])
    letter2 = cell2[0]
    number2 = int(cell2[1])
    return (abs(ord(letter2)-ord(letter1)) + abs(number2-number1)) % 2 == 0