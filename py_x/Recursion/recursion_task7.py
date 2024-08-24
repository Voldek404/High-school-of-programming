def recursion_second_max(list, i=None, max_1=None, count=None):
    if len(set(list)) == 1:
        return None
    if i is None:
        i = 0
    if max_1 is None:
        max_1 = 0
    if count is None:
        count = 0
    if list[i] > max_1:
        max_1 = list[i]
    if i >= len(list) - 1:
        list.remove(max_1)
        if len(list) == 1:
            return list[0]
        count += 1
        if count == 2:
            return max_1
        max_1 = 0
        i = 0
    return recursion_second_max(list, i + 1, max_1, count)
