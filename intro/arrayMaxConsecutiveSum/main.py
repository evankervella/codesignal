def arrayMaxConsecutiveSum(inputArray: list, k: int) -> int:
    last_sum = sum(inputArray[:k])
    max_consecutive_sum = last_sum
    for i in range(1, len(inputArray)-k+1):
        last_sum += inputArray[i+k-1] - inputArray[i-1]
        if last_sum > max_consecutive_sum:
            max_consecutive_sum = last_sum
    return max_consecutive_sum