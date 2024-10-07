def MisterRobot(N: int, data: list) -> bool:
    list_2 = sorted(data)
    iteration = 0
    while list_2 != data:
        for j in range(0, N - 3):
            while data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                iteration += 1
                if data[j] > data[j + 1] or data[j + 1] > data[j + 2]:
                    data[j], data[j + 1], data[j + 2] = data[j + 1], data[j + 2], data[j]
                    if iteration >= 20:
                        return data == list_2
    return data == list_2


