def MisterRobot(N, data):
    list_2 = sorted(data)
    while list_2 != data:
        for j in range(0, 4):
            while data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                if data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                    data[j], data[j + 1], data[j + 2] = data[j + 1], data[j + 2], data[j]
    return data == list_2


data = [1, 3, 4, 5, 6, 2, 7]
N = 7
print(MisterRobot(N, data))