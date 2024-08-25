def recursion_second_max(list, **kwargs):
    if len(set(list)) == 1:
        return None
    i = kwargs.get('i', 0)
    max = kwargs.get('max', 0)
    count = kwargs.get('count', 0)
    if count is None:
        count = 0
    if list[i] > max:
        max = list[i]
    if i >= len(list) - 1:
        list.remove(max)
        if len(list) == 1:
            return list[0]
        count += 1
        if count == 2:
            return max
        max = 0
        i = 0
    return recursion_second_max(list, i=i + 1,max=max, count=count)
