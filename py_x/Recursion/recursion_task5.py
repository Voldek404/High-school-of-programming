def recursion_print_even(list_1):
    if len(list_1) == 0:
        return 
    if list_1[0] % 2 == 0:
        print(list_1[0])
    recursion_print_even(list_1[1:])




