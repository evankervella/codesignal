def areSimilar(a, b):
    if a == b:
        return True
    for i in range(len(a)):
        if a[i] != b[i]:
            for j in range(len(a)):
                if a[j] != b[j]:
                    a_ = a.copy()
                    a_[i], a_[j] = a_[j], a_[i]
                    if a_ == b:
                        return True
    return False