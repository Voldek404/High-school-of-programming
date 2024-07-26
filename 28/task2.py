def odometer(oksana):
    car_range = 0
    for i in range(len(oksana) - 2):
        car_range += oksana[i] * oksana[i + 1]
    return car_range


