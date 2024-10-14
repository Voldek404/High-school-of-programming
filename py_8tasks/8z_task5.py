def massdriver_helper(activate: list, index: int, activate_dict) -> int:
    if index == len(activate):
        return -1
    item = activate[index]
    if item in activate_dict.keys():
        activate_dict[activate[index]] = activate_dict.get(item, 0) + 1
        if activate_dict[item] > 1:
            return activate.index(item)
    return massdriver_helper(activate, index + 1, activate_dict)


def massdriver(activate, activate_dict):
    return massdriver_helper(activate, 0, activate_dict)


activate = [1, 1, 3, 4, 5, 6, 90, 65, 78, 90]
activate_dict = dict.fromkeys(activate, 0)

