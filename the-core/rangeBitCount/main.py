def rangeBitCount(a: int, b: int) -> int:
    list_bin = ''
    for i in range(a, b+1):
        list_bin += bin(i)
    count = 0
    for b in list_bin:
        if b == '1':
            count += 1
    return count