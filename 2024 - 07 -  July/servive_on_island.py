import math

def minfood(N, S, M):
    food = 0
    if M>N:
        return -1
    else:
        food = math.ceil((M*S)/N)

    return food

N = 9 # max food you can buy each day
S = 10 # days to servive
M = 8 # unit of food each day to eat
print(minfood(N, S, M))