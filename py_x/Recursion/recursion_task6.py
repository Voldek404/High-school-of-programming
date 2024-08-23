def recursion_print_even(list_1: list):
    if not list_1:
        return
    if (len(list_1) - 1) % 2 == 0:
        print(list_1[-1])
    list_1.pop()
    recursion_print_even(list_1)


