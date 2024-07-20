import math

def minfood(N, S, M):
    food = 0
    if M>N:
        return -1
    else:
        food = math.ceil((M*S)/N)
    if food >= S-1:
        return -1
    return food

N = 10 # max food you can buy each day
S = 10 # days to servive
M = 3 # unit of food each day to eat
print(minfood(N, S, M))