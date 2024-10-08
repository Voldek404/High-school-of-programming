def white_walker_helper(village: str, index: int, digit_sum: int, equal_sum: int, field_gaps:list):
    if index == len(village):
        return
    if village[index].isdigit():
        field_gaps.append(index)
    if len(field_gaps) == 2 and (int(village[field_gaps[0]])+int(village[field_gaps[1]])) == 10:
        return village[field_gaps[0]: field_gaps[1]].count('=') >= 3
        field_gaps = []
    elif len(field_gaps) == 2:
        field_gaps.pop(0)
    return white_walker_helper(village, index + 1, digit_sum, equal_sum, field_gaps)


def white_walker(village: str) -> bool:
    return white_walker_helper(village, 0, 0, 0, [])