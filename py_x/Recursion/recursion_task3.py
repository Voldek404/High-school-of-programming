def list_len(list_1):
    if not list_1:
        return 0
    else:
        list_1.pop(0)
    return  list_len(list_1) + 1