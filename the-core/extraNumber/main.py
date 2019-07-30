def extraNumber(a: int, b: int, c: int) -> int:
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a