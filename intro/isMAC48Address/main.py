import re

def isMAC48Address(inputString: str) -> bool:
    pattern = "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"
    if re.match(pattern, inputString.lower()):
        return True
    return False