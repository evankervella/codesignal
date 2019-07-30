def killKthBit(n, k):
    return n if k > len(bin(n)) else int(''.join(list(bin(n))[2:len(bin(n))-k]+['0']+list(bin(n))[len(bin(n))-k+1:]), 2)
