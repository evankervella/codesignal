def isPalindrome(st: str) -> bool:
    st = list(st)
    n = len(st)
    for i in range(n//2):
        if st[i] != st[n-1-i]:
            return False
    return True

def buildPalindrome(st: str) -> str:
    if isPalindrome(st):
        return st
    n = len(st)
    r_st = st[::-1]
    for i in range(n):
        print(r_st[len(st)-i:])
        if isPalindrome(st+r_st[len(st)-i:]):
            return st+r_st[len(st)-i:]