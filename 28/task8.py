def SumOfThe(N,  data):
    for i in data:
        data_raw = data[:]
        data_raw.remove(i)
        if i == sum(data_raw):
            break
    return i
