def white_walkers(village : str) -> bool:
    if village == '':
        result = False
    white_walker = "==="
    if village.count(white_walker) >= 1 and village.index(white_walker) != 0 and village.index(white_walker) +3 != len(village) :
        result = True
    else:
        result = False
    return result
