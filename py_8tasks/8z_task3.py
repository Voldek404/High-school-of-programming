def eec_help_helper(arr1: list, arr2: list, index: int, arr1_dict: dict, arr2_dict: dict) -> bool:
    if len(arr1) != len(arr2):
        return False
    if index == len(arr1) == len(arr2):
        return arr1_dict == arr2_dict
    arr1_dict[index + 1] = arr1[index]
    arr2_dict[index + 1] = arr2[index]
    return eec_help_helper(arr1, arr2, index + 1, arr1_dict, arr2_dict)


def eec_help(arr1: list, arr2: list):
    return eec_help_helper(arr1, arr2, 0, {}, {})


arr1, arr2 = sorted(arr1), sorted(arr2)

