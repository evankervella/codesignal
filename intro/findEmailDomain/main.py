def findEmailDomain(address: str) -> str:
    address = list(address)
    for i in range(len(address)-1, -1, -1):
        if address[i] == '@':
            return ''.join(address[i+1:])