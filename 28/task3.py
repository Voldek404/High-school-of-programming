import random


def ConquestCampaign(N, M, L, battalion):
    training_space = []  # forming a training space
    for i in range(1, N + 1):
        a1 = []
        for j in range(1, M + 1):
            a1.append('0')
        training_space.append(a1)
        
    for i in range(L):  # forming first day landing coordinates
        battalion.append(random.randint(1,N))
        battalion.append(random.randint(1,M))

    for i in range(0, L * 2, 2):  # paint first day points
        x = battalion[i] - 1
        y = battalion[i + 1] - 1
        training_space[x][y] = 1

    day = 1

    while True:
        done = False

        for i in range(N):
            for j in range(M):
                if training_space[i][j] == day:  # setting moving frames according to range from edges
                    if i > 0 and training_space[i - 1][j] == 0:
                        training_space[i - 1][j] = day + 1
                        training_space[i][j] = 1
                        done = True
                    if i < N - 1 and training_space[i + 1][j] == 0:
                        training_space[i + 1][j] = day + 1
                        training_space[i][j] = 1
                        done = True
                    if j > 0 and training_space[i][j - 1] == 0:
                        training_space[i][j - 1] = day + 1
                        training_space[i][j] = 1
                        done = True
                    if j < M - 1 and training_space[i][j + 1] == 0:
                        training_space[i][j + 1] = day + 1
                        training_space[i][j] = 1
                        done = True
        

        if not done:
            break
    day += 1

            


    return day
