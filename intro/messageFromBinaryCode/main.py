def messageFromBinaryCode(code: str) -> str:
    return ''.join([chr(int(code[8*i:8*i+8], 2)) for i in range(len(code)//8)])