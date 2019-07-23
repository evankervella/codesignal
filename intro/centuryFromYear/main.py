def centuryFromYear(year: int) -> int:
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century