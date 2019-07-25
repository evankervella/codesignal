import re

def sumUpNumbers(inputString: str) -> int:
    extract = re.split('[^0-9]', inputString)
    numbers = [int(char) for char in extract if char.isdigit()]
    return(sum(numbers))