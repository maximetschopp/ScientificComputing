def find(seq, val):
    out = []
    for i in range(len(seq)):
        if seq[i] == val:
            out.append(i)
    return out

def filter(seq, ignore):
    out = []
    for item in seq:
        if item not in ignore:
            out.append(item)
    return out

def common(seq1, seq2):
    out = []
    for item in seq1:
        if item in seq2 and item not in out:
            out.append(item)
    return out