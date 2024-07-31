def PrintingCosts(Line):
    toner_sum = 0
    for i in Line:
        if i in sample_dict:
            toner_sum += int(sample_dict[i])
        else:
            toner_sum += 23
    return toner_sum
