def makeArrayConsecutive2(statues: list) -> int:
    min_statues = min(statues)
    max_statues = max(statues)
    return max_statues-min_statues-len(statues)+1