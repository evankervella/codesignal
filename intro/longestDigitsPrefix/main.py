def longestDigitsPrefix(inputString: str) -> str:
    prefix = []
    inputString = list(inputString)
    i = 0
    while inputString[i].isdigit() and i < len(inputString)-1:
        prefix.append(inputString[i])
        i += 1
    if i == len(inputString)-1:
        if inputString[i].isdigit():
            prefix.append(inputString[i])
    return ''.join(prefix)