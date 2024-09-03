def recursion_print_even_index_helper(list_1, index:int):
    if len(list_1) == 0:
        return False
    if index >= len(list_1):
        return 
    print(list_1[index])
    return recursion_print_even_index_helper(list_1,index + 2)
    
def recursion_print_even_index(list_1):
    return recursion_print_even_index_helper(list_1, 0)



