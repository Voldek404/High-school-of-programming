def odometer(oksana):
    car_range = oksana[0] * oksana[1]
    i = len(oksana) - 1
    while i != 1:
        car_range += (oksana[i] - oksana[i - 2]) * oksana[i - 1]
        i -= 2
    return car_range


