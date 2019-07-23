def isBeautifulString(inputString: str) -> bool:
    ord_a = ord('a')
    letters_count = {}
    for i in range(26):
        letters_count[chr(i+ord_a)] = 0
    for char in inputString:
        if char.isalpha():
            letters_count[char] += 1
    last_occurency = 50
    for letter in sorted(letters_count):
        if letters_count[letter] > last_occurency:
            return False
        last_occurency = letters_count[letter]
    return True