def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
    result = False
    map_2_string = ''
    if H1 < H2:
        result = False
    S1 = S1.split()
    S2 = S2.split()
    for i in range(0, len(S2)):
        map_2_string += S2[i]
    index_list = []
    for n in range(0, W1 - 1):
        index_list.append(n)
    for i in range(0, len(S2) - 1):
        for j in range(0, len(S1)):
            if S2[i] in S1[j]:
                for m in index_list:
                    first_index = m
                    second_index = m + W2
                    map_1_string = ''
                    for k in (S1)[j:j + W2]:
                        map_1_string += k[int(m):int(second_index)]
                        if map_1_string == map_2_string:
                            result = True
                            break
            else:
                continue
    return result
