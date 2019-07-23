def extractEachKth(inputArray: list, k: int) -> list:
    index_to_drop = []
    index = -1
    while index < len(inputArray)-k:
        index += k
        index_to_drop.append(index)
    return [inputArray[x] for x in range(len(inputArray)) if x not in index_to_drop]