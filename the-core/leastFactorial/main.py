def leastFactorial(n: int) -> int:
    m = 1
    k = 1
    while k < n:
        m += 1
        k *= m
    return k