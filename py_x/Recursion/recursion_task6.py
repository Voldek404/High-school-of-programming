def recursion_print_even(list_1, list_2=None, i=None):
    if list_2 is None:
        list_2 = []
    if i is None:
        i = 0
    if i >= len(list_1):
        return list_2
    print(i)
    return recursion_print_even(list_1, list_2, i + 2)


