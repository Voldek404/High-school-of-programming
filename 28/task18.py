def MisterRobot(N: int, data: list) -> bool:
    list_2 = sorted(data)
    for i in range(0, N - 1):
        if data[i + 1] > data[i + 2]:
            return data == list_2
    while list_2 != data:
        for j in range(0, 4):
            while data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                if data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                    data[j], data[j + 1], data[j + 2] = data[j + 1], data[j + 2], data[j]
    return data == list_2



