def countSumOfTwoRepresentations2(n: int, l: int, r: int) -> int:
    if n//2 not in range(l, r+1):
        return 0
    return n//2 - max(l, n-r) + 1