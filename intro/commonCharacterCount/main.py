def commonCharacterCount(s1: str, s2: str) -> int:
    count = 0
    if len(s1) > len(s2):
        s = list(s1)
        s_ = list(s2)
    else:
        s = list(s2)
        s_ = list(s1)
    for i in range(len(s_)):
        for j in range(len(s)):
            if s_[i] == s[j]:
                count += 1
                del(s[j])
                break
    return count