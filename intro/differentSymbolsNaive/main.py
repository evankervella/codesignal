def differentSymbolsNaive(s: str) -> int:
    known_chars = []
    for char in s:
        if char not in known_chars:
            known_chars.append(char)
    return len(known_chars)