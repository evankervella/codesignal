def digitsProduct(product: int) -> int:
    if product < 10:
        return product if product > 0 else 10
    output = ""
    for i in range(9,1,-1):
        while product % i == 0:
            product /= i
            output = chr(ord('0')+i) + output;
    if product != 1:
        return -1
    return int(output)