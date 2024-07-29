def PatternUnlock(N, hits):
    hits_sum = 0
    for i in range(N):
        if abs(hits[i] - hits[i + 1]) == 4 or abs(hits[i] - hits[i + 1]) == 2 or abs(hits[i] - hits[i + 1]) == 7 or abs(
                hits[i] - hits[i + 1]) == 5:
            hits_sum += 1.414213
        elif hits[i] == 6 and hits[i + 1] == 1 or hits[i + 1] == 6 and hits[i] == 1:
            hits_sum += 1
        else:
            hits_sum += 1
    hits_sum = round(hits_sum, 5)
    print(hits_sum)
    for i in str(hits_sum):
        res_hits_sum = str(hits_sum).replace('.', '')
        if i == 0:
            res_hits_sum = str(hits_sum).replace('0', '')
    return res_hits_sum



