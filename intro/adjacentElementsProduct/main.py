def adjacentElementsProduct(inputArray: list) -> int:
    n = len(inputArray)
    biggest_product = -1e6
    for i in range(n-1):
        if inputArray[i]*inputArray[i+1] > biggest_product:
            biggest_product = inputArray[i]*inputArray[i+1]
    return biggest_product