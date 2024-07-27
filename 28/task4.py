def MadMax(N, list_proto):
    list_max = [max(list_proto)]
    list_proto.remove(max(list_proto))
    list_left = sorted(list_proto[: int(N / 2)])
    list_right = sorted(list_proto[int(N / 2):], key=None, reverse=True)
    return list_left + list_max + list_right
