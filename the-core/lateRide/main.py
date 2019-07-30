def lateRide(n: int) -> int:
    h = n // 60
    m = n % 60
    return sum([int(digit) for digit in str(h)+str(m)])