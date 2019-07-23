def depositProfit(deposit: int, rate: int, threshold: int) -> int:
    year = 0
    while deposit < threshold:
        year += 1
        deposit += deposit * rate/100
    return year