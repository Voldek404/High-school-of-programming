def Unmanned(road_length, tl_number, track):
    total_time = 0
    current_time = 0

    for i in range(tl_number):
        traffic_light_location, red_tl__time, green_tl_time = track[i]
        distance = traffic_light_location - current_time

        if distance > 0:
            total_time += distance

        if total_time < road_length:
            tl_cycles = (total_time + red_tl__time) // (red_tl__time + green_tl_time)
            remainder = total_time % (red_tl__time + green_tl_time)

            if remainder < red_tl__time:
                total_time += red_tl__time - remainder

        current_time = traffic_light_location

    total_time += road_length - current_time

    return total_time
