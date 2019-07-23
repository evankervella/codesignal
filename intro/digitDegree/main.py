def digitDegree(n: int) -> int:
    count = 0
    if len(str(n)) == 1:
        return count 
    else:
        count += 1
        while len(str(sum(int(digit) for digit in str(n)))) > 1:
            count += 1
            n = sum(int(digit) for digit in str(n))
    return count