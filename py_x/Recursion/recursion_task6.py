def recursion_print_even(list_1, i=0, even_indexes=None):
    if even_indexes is None:
        even_indexes= []
    elif i >= len(list_1):
        return even_indexes
    elif i % 2 == 0:
        even_indexes.append(list_1[i])
    return recursion_print_even(list_1, i + 1, even_indexes)


