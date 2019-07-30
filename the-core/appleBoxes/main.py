def appleBoxes(k: int) -> int:
    result = 0
    for i in range(1, k+1):
        if i%2 == 0:
            result += i**2
        else:
            result -= i**2
    return result