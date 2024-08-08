def MaximumDiscount(N, price):
    money_savings = 0
    raw_price = sorted(price, reverse=True)
    if N > 3:
        flag = True
    elif N == 3:
        money_savings = raw_price[N - 1]
    elif N < 3:
        money_savings = 0
    for i in range(2, N, 3):
        if flag:
             money_savings += raw_price[i]
    money_savings_3 = money_savings

    return money_savings
