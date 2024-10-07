def BigMinus(string_1, string_2):
    if len(string_2) > len(string_1):
        string_2, string_1 = string_1, string_2
    string_2 = "0" * (len(string_1) - len(string_2)) + string_2
    string_1 = list(string_1)
    string_2 = list(string_2)
    result = ''
    if string_1 == string_2:
        result = '0'
    elif len(string_1) == len(string_2) == 1:
        result = str(abs(int(string_1[0]) - int(string_2[0])))
    else:
        borrow = 0
        for i in range(len(string_1) - 1, -1, -1):
            d_1 = int(string_1[i])
            d_2 = int(string_2[i])
            diff = d_1 - d_2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result = str(diff) + result

        result = result.lstrip('0')
    return result


