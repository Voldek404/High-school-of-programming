def Keymaker(k: int) -> str:
    doors_list = []
    for i in range(0, k):
        doors_list.append(0)
    n = 2
    for i in range(0, k):
        if doors_list[i] == 0:
            doors_list[i] = 1
    for i in range(1, k, n):
        if doors_list[i] == 1:
            doors_list[i] = 0
    while n<k:
        n+=1
        for i in range(n-1, k,n):
            if doors_list[i] == 1:
                doors_list[i] = 0
            elif doors_list[i] == 0:
                doors_list[i] = 1
    result = ''.join(str(el) for el in doors_list)
    return result
