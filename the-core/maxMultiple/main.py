def maxMultiple(divisor: int, bound: int) -> int:
    divisors = [n for n in range(bound+1) if n%divisor==0]
    return max(divisors)