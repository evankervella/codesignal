def arrayChange(inputArray: list) -> int:
    number_moves = 0
    for i in range(len(inputArray)-1):
        diff_to_consider = max(0, inputArray[i]-inputArray[i+1]+1)
        number_moves += diff_to_consider
        inputArray[i+1] += diff_to_consider
    return number_moves