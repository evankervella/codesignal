def evenDigitsOnly(n: int) -> bool:
    digits = [int(x) for x in str(n)]
    for digit in digits:
        if digit % 2 == 1:
            return False
    return True