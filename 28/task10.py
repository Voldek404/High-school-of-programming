def PrintingCosts(Line):
    toner_sum = 0
    for i in range(1,len(Line)+1):
        if sample_dict[i] in sample_dict.values():
            toner_sum += sample_dict[i]
        else:
            toner_sum += 23
    return toner_sum
