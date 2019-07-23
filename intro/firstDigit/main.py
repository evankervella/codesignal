def firstDigit(inputString: str) -> str:
    for char in inputString:
        if char.isdigit():
            return char