def palindromeRearranging(inputString):
    for char in inputString:
        if inputString.count(char) % 2 == 0:
            inputString = inputString.replace(char,'')
    if len(inputString) == 0 or len(inputString) == 1:
        return True
    elif len(inputString) % 2 == 1:
        return len(inputString) == inputString.count(inputString[0])
    return False