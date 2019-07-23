def checkPalindrome(inputString: str) -> bool:
    n = len(inputString)
    for i in range(n//2):
        if inputString[i] != inputString[n-1-i]:
            return False
    return True