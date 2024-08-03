def UFO(N, data, octal):
    result = []
    for i in range(0, N - 1):
        if octal:
            result.append(int(str(data[i]), 8))
        else:
            result.append(int(str(data[i]), 16))
    return result
