def recursion_print_even(list_1, i=0, even_numbers=None):
    if even_numbers is None:
        even_numbers = []
    elif i >= len(list_1):
        return even_numbers
    elif list_1[i] % 2 == 0:
        even_numbers.append(list_1[i])
    return recursion_print_even(list_1, i + 1, even_numbers)


