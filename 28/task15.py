def TankRush(map_1, map_2):
    result = 0
    if map_1[0] < map_2[0]:
        result = False
    map_1_string = ''
    map_2_string = ''
    for i in range(2, len(map_2)):
        map_2_string += map_2[i]
    for i in range(2, len(map_2)):
        for j in range(2, len(map_1)):
            if map_2[i] in map_1[j]:
                first_index = map_1[j].index(map_2[i])
                second_index = first_index + map_2[1]
                map_1_string = ''
                for k in (map_1)[j:j + map_2[1]]:
                    map_1_string += k[first_index:second_index]
                if map_1_string == map_2_string:
                    result = True
                    break
            else:
                continue

    return result
