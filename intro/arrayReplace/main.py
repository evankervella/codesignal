def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x==elemToReplace else x for x in inputArray]