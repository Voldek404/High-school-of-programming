def ShopOLAP(N: int, items):
    list_2 = []
    duplicates = []
    for j in range(0, N):
        list_2.append(items[j].split())
    flat_list = [item for sublist in list_2 for item in sublist]
    for i in range(0, len(flat_list), 2):
        for k in range(i + 2, len(flat_list)):
            if flat_list[i] == flat_list[k]:
                flat_list[i + 1] = int(flat_list[i + 1]) + int(flat_list[k + 1])
                duplicates.append(k)
                duplicates.append(k+1)
    for index in sorted(duplicates, reverse=True):
        flat_list.pop(index)
    dict_from_list = {flat_list[i]: int(flat_list[i + 1]) for i in range(0, len(flat_list), 2)}
    sorted_dict = dict(sorted(dict_from_list.items(), key=lambda item: item[0]))
    result = [f"{key} {value}" for key, value in sorted_dict.items()]
    return result
