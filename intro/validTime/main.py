def validTime(time: str) -> bool:
    return int(''.join(time[:2])) >= 0 and int(''.join(time[:2])) < 24 and int(''.join(time[-2:])) >= 0 and int(''.join(time[-2:])) < 60