def electionsWinners(votes: list, k: int) -> int:
    still_in_race = 0
    winner_yet = max(votes)
    for vote in votes:
        if vote+k > winner_yet:
            still_in_race += 1
    if k == 0:
        count_winners = 0
        for vote in votes:
            if vote == winner_yet:
                count_winners += 1
        if count_winners == 1:
            return 1
        else:
            return 0
    return still_in_race