def digital_rain_helper(col: str, transformed_list: list, sum_dict: dict, summa: int, sub_col: list, index: int) -> str:
    if index >= len(transformed_list):
        if sub_col == []:
            return ''
        elif (("".join(sub_col)).count('1') == ("".join(sub_col)).count('0')):
            return(sub_col[len(sub_col)-1])
        else:
            return (max(sub_col))
    value = transformed_list[index]
    summa += value
    if summa in sum_dict:
        start_index = sum_dict[summa] + 1
        sub_col.append(col[start_index:index + 1])
    else:
        sum_dict[summa] = index
    return digital_rain_helper(col, transformed_list, sum_dict, summa, sub_col, index + 1)


def digital_rain(col: str, transformed_list: list):
    return digital_rain_helper(col, transformed_list, {0: -1}, 0, [], 0)


transformed_list = [1 if bit == '1' else -1 for bit in col]

