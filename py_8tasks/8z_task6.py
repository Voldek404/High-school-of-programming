def trc_sort_helper(trc: list, index: int, array_for_0, array_for_1, array_for_2) -> list:
    if index == len(trc):
        return array_for_0 + array_for_1 + array_for_2
    if trc[index] == 0:
        array_for_0.append(trc[index])
    elif trc[index] == 1:
        array_for_1.append(trc[index])
    elif trc[index] == 2:
        array_for_2.append(trc[index])
    return trc_sort_helper(trc, index + 1, array_for_0, array_for_1, array_for_2)

def trc_sort(trc):
    return trc_sort_helper(trc, 0, [], [], [])