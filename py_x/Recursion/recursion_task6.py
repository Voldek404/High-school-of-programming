def recursion_print_even(list_1, *args, **kwargs):
    if not args:
        list_2 = []
    else:
        list_2 = args[0]
    i = kwargs.get('i', 0)
    if i >= len(list_1):
        return list_2
    list_2.append(i)

    return recursion_print_even(list_1, list_2, i=i + 2)


