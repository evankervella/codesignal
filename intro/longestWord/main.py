import re

def longestWord(text: str) -> str:
    s = re.split('[^a-zA-Z]', text)
    return max(s, key=len)