def isLucky(n: int) -> bool:
    l = list(str(n))
    n1 = l[:int(len(l)/2)]
    n2 = l[int(len(l)/2):]
    sum_n1 = 0
    for elt in n1:
        sum_n1 += int(elt)
    sum_n2 = 0
    for elt in n2:
        sum_n2 += int(elt)
    print(sum_n1, sum_n2)
    return sum_n1 == sum_n2