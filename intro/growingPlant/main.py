def growingPlant(upSpeed: int, downSpeed: int, desiredHeight: int) -> int:
    days = 0
    height = 0
    while height < desiredHeight:
        days += 1
        height += upSpeed
        if height >= desiredHeight:
            return days
        height -= downSpeed
    return days