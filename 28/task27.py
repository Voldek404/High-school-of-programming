def rule_one(football_list: list, N) -> bool:
    indices_list = []
    football_list_sorted = sorted(football_list)
    for i in range(0, N):
        if football_list[i] != football_list_sorted[i]:
            indices_list.append(i)
    if len(indices_list) == 2:
        for i in indices_list:
            football_list[indices_list[0]], football_list[indices_list[1]] = football_list[indices_list[1]], \
            football_list[indices_list[0]]
            return football_list == football_list_sorted


def rule_two(football_list: list, N) -> bool:
    indices_list = []
    football_list_sorted = sorted(football_list)
    for i in range(0, N - 1):
        if football_list[i] != football_list_sorted[i]:
            indices_list.append(i)
    for i in indices_list:
        slice = football_list[indices_list[0]:indices_list[1] + 1]
        slice.reverse()
        football_list = football_list[:indices_list[0]] + list(slice) + football_list[indices_list[1] + 1:]
        return football_list == football_list_sorted

def Football(football_list: list, N: int) -> bool:
    if rule_one(football_list, N):
        return True
    elif rule_two(football_list, N):
        return True
    else:
        return False
