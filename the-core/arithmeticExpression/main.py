def arithmeticExpression(a: int, b: int, c: int) -> bool:
    if a+b == c or a-b == c or a*b == c or a/b == c:
        return True
    return False