def allLongestStrings(inputArray: list) -> list:
    longest = 0
    for elt in inputArray:
        if len(elt) > longest:
            longest = len(elt)
    outputArray = []
    for elt in inputArray:
        if len(elt) == longest:
            outputArray.append(elt)
    return outputArray