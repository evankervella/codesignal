def almostIncreasingSequence(sequence: list) -> bool:
    neg_count = []
    for i in range(len(sequence)-1):
        if sequence[i+1]-sequence[i] <= 0:
            neg_count.append(1)
            if sum(neg_count) > 1:
                return False
        neg_count.append(0)
    if sum(neg_count) == 1:
        tmp_seq = sequence.copy()
        del(tmp_seq[neg_count.index(1)])
        for i in range(len(tmp_seq)-1):
            if tmp_seq[i+1]-tmp_seq[i] <= 0:
                tmp_seq = sequence.copy()
                del(tmp_seq[neg_count.index(1)+1])
                for i in range(len(tmp_seq)-1):
                    if tmp_seq[i+1]-tmp_seq[i] <= 0:
                        return False
    return True