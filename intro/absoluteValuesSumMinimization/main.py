def absoluteValuesSumMinimization(a: list) -> int:
    weights_barycenter = math.inf
    barycenter = 0
    for i in range(len(a)):
        weights = 0
        for j in range(len(a)):
            if j != i:
                weights += abs(a[j]-a[i])
        if weights < weights_barycenter:
            weights_barycenter = weights
            barycenter = a[i]
    return barycenter