def recursion_print_even(list_1, *args, **kwargs):
    if not args:
        list_2 = []
    else:
        list_2 = args[0] 
    i = kwargs.get('i', 0)
    if i >= len(list_1):
        return list_2

    if list_1[i] % 2 == 0:
        list_2.append(list_1[i])

    return recursion_print_even(list_1, list_2, i=i + 1)




