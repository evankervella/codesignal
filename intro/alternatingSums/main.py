def alternatingSums(a):
    result = []
    result.append(sum(a[0::2]))
    result.append(sum(a[1::2]))
    return result