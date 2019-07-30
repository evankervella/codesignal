def variableName(name: str) -> bool:
    if name[0].isdigit():
        return False
    for char in name:
        if not ((char.isdigit()) or (char.isalpha()) or (char == '_')):
            return False
    return True