def MadMax(N, list_proto):
    list_prom = sorted(list_proto)
    list_max = [max(list_prom)]
    list_prom.remove(max(list_proto))
    list_left = list_prom[: int(N / 2)]
    list_right = sorted(list_prom[int(N / 2):], key=None, reverse=True)
    return list_left + list_max + list_right
