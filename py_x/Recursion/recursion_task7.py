def recursion_second_max_helper(list, index,max,count, new_list):
    if new_list[index] > max:
        max = new_list[index]
    if index >= len(new_list) - 1:
        new_list.remove(max)
        if len(new_list) == 1:
            return new_list[0]
        count += 1
        if count == 2:
            return max
        max = 0
        index = 0
    return recursion_second_max_helper(list,index=index + 1,max=max, count=count, new_list = new_list)
    
def recursion_second_max(list):
    return recursion_second_max_helper(list, 0,0,0,list)
