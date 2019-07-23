def bishopAndPawn(bishop: str, pawn: str) -> bool:
    letter1 = bishop[0]
    number1 = int(bishop[1])
    letter2 = pawn[0]
    number2 = int(pawn[1])
    return abs(ord(letter2)-ord(letter1)) == abs(number2-number1)
