def MisterRobot(N, data):
    list_2 = sorted(data)
    iterations = 0
    while data!= list_2 and iterations < 1000:
        swapped = False
        for j in range(0, len(data) - 2):
            if data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swapped = True
                if data[j + 1] > data[j + 2]:
                   data[j + 1], data[j + 2] = data[j + 2], data[j + 1]
                   swapped = True
        if not swapped:
                break
        iterations += 1
    return data == list_2
