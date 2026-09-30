def speeding(speeds, limit):

    speed_exeeded = []
    speed_exceeded_count = 0

    for speed_rate in speeds:
        if speed_rate > limit:
            speed_exeeded += [speed_rate]
            speed_exceeded_count += 1 

    if len(speed_exeeded) == 0:
        return 0, 0

    speed_exeeded_average = sum(speed_exeeded) / len(speed_exeeded)

    return len(speed_exeeded), speed_exeeded_average - limit

        



print(speeding([50, 60, 55], 60))
print(speeding([58, 50, 60, 55], 55))
print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([100, 105, 95, 102], 100))
print(speeding([40, 45, 44, 50, 112, 39], 55))