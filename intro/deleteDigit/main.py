def deleteDigit(n: int) -> int:
    biggest_digit = 0
    n = list(str(n))
    for i in range(len(n)):
        m = [digit for digit in n]
        del m[i]
        m = int(''.join(m))
        if m > biggest_digit:
            biggest_digit = m
    return biggest_digit