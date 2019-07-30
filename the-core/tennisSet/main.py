def tennisSet(score1: int, score2: int) -> bool:
    if score1 > 7 or score2 > 7:
        return False
    if score1 == 6 and score2 < 5 or score2 == 6 and score1 < 5:
        return True
    if score1 == 7 and (5 <= score2 and score2 < 7) or score2 == 7 and (5 <= score1 and score1 < 7):
        return True
    return False