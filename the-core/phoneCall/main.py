def phoneCall(min1: int, min2_10: int, min11: int, s: int) -> int:
    if s < min1:
        return 0
    if s-min1 < (10-2+1) * min2_10:
        return (s-min1)//min2_10 + 1
    else:
        return ((s-min1)-((10-2+1)*min2_10)) // min11 + 10