def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i+1]-inputArray[i]) > max_diff:
            max_diff = abs(inputArray[i+1]-inputArray[i])
    return max_diff