def avoidObstacles(inputArray):
    for i in range(1, max(inputArray)):
        dividers = any([x for x in inputArray if not x%i])
        if not dividers:
            return i
    return max(inputArray)+1