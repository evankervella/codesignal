def magicalWell(a: int, b: int, n: int) -> int:
    sum_ = 0
    for i in range(n):
        sum_ += (a+i)*(b+i)
    return sum_