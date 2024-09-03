def recursion_print_even_index_helper(list_1, index):
    if index >= len(list_1):
        return 
    if list_1[index] % 2 == 0:
        print(index)
    return recursion_print_even_index_helper(list_1,index + 1)
    
def recursion_print_even_index(list_1):
    return recursion_print_even_index_helper(list_1, 0)



