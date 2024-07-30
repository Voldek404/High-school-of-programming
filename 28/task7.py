def WordSearch(length, input_string, subs):
    search_list = []
    splitted_string = input_string.split()
    while splitted_string != []:
        if len(splitted_string[0]) == length and len(splitted_string) == 1 :
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
            break
        if len(splitted_string[0]) == length:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
        elif len(splitted_string) == 1 and len(splitted_string[0]) < length:
            search_list.append(splitted_string[0] + ' ' * (
                    length - len(splitted_string[0])))
            splitted_string.pop(0)
            break
        elif len(splitted_string) == 1 and len(splitted_string[0]) > length:
            search_list.append(splitted_string[0][:length ])
            splitted_string[0] = splitted_string[0][length:]
            search_list.append(splitted_string[0][:length - 1] + ' ' * (
                    length - len(splitted_string[0])))
            break
        elif len(splitted_string[0] + splitted_string[1]) < length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' * (
                    length - len(splitted_string[0] + splitted_string[1] + ' ')))
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) < length and len(splitted_string[0] + splitted_string[1]) > length:
            search_list.append(splitted_string[0] + ' ' * (
                    length - len(splitted_string[0])))
            splitted_string.pop(0)
        elif len(splitted_string[0] + splitted_string[1]) == length:
            search_list.append(splitted_string[0])
            splitted_string.pop(0)
        elif len(splitted_string) > 2 and len(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2]) == length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2])
            splitted_string.pop(0)
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string) > 2 and len(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2]) < length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' + splitted_string[2] + ' ' * (
                    length - len(splitted_string[0]) - len(splitted_string[1] - len(splitted_string[2]))))
            splitted_string.pop(0)
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) > length:
            search_list.append(splitted_string[0][:length ])
            splitted_string[0] = splitted_string[0][length:]
        elif len(splitted_string[0] + splitted_string[1]) < length:
            search_list.append(splitted_string[0] + ' ' + splitted_string[1] + ' ' * (
                    length - len(splitted_string[0] + splitted_string[1] + ' ')))
            splitted_string.pop(0)
            splitted_string.pop(0)
        elif len(splitted_string[0]) < length:
            search_list.append(splitted_string[0] + ' ' * (
                    length - len(splitted_string[0])))
            splitted_string.pop(0)
    result_string = ''
    for rows in search_list:
        if subs in rows.split():
            result_string += '1'
        else:
            result_string += '0'
    return result_string
