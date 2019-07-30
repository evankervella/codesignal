def increaseNumberRoundness(n: int) -> bool:
    n = list(str(n))
    i = len(n)-1
    while n[i] == '0' and i >= 0:
        i -= 1
    if i == -1:
        return False
    for j in range(i-1, -1, -1):
        if n[j] == '0':
            return True
    return False