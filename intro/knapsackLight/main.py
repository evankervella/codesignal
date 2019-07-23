def knapsackLight(value1: int, weight1: int, value2: int, weight2: int, maxW: int) -> int:
    if weight1 > maxW and weight2 > maxW:
        return 0
    elif weight1 > maxW:
        return value2
    elif weight2 > maxW:
        return value1
    elif weight1+weight2 <= maxW:
        return value1+value2
    else:
        return max(value1, value2)