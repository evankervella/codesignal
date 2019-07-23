def sortByHeight(a):
    a_ = [elt for elt in a if elt not in [-1]]
    a_.sort()
    list_idx = []
    for i in range(len(a)):
        if a[i] == -1:
            a_.insert(i,-1)
    return a_