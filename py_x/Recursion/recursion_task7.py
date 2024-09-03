def recursion_second_max_helper(list, index,max,count):
    if list[index] > max:
        max = list[index]
    if index >= len(list) - 1:
        list.remove(max)
        if len(list) == 1:
            return list[0]
        count += 1
        if count == 2:
            return max
        max = 0
        index = 0
    return recursion_second_max_helper(list,index=index + 1,max=max, count=count)
    
def recursion_second_max(list):
    return recursion_second_max_helper(list, 0,0,0)
