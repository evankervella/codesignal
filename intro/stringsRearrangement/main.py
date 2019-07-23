import itertools

def diffByOne(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    count = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            count += 1
    return count == 1

def stringsRearrangement(inputArray: list) -> bool:
    permutations = [p for p in itertools.permutations(inputArray)]
    for p in permutations:
        b = True
        for i in range(len(p)-1):
            if not diffByOne(p[i], p[i+1]):
                b = False
                break
        if b:
            return b
    return b