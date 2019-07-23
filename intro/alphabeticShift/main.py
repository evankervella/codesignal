def alphabeticShift(inputString: str) -> str:
    outputString = []
    for char in inputString:
        if char == 'z':
            outputString.append('a')
        else:
            outputString.append(chr(ord(char)+1))
    outputString = ''.join(outputString)
    return outputString