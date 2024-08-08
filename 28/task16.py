def MaximumDiscount(N, price):
    money_savings = 0
    flag = 0
    raw_price = sorted(price, reverse=True)
    if N >= 3:
        flag = True
    elif N < 3:
        money_savings = 0
    for i in range(2, N, 3):
        if flag:
             money_savings += raw_price[i]

    return money_savings
