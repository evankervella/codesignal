def arrayPacking(a: list) -> int:
    bin_a = ''
    for number in a:
        bin_number = '0' * (8-len(bin(number)[2:])) + bin(number)[2:]
        bin_a = bin_number + bin_a
    return int(bin_a, 2)