import math

def minfood(N, S, M):
    sun = 1
    food = math.ceil((M*S)/N)
    if food >= S-sun:
        return -1
    return food

N = 20 # max food you can buy each day
S = 10 # days to servive
M = 30 # unit of food each day to eat
print(minfood(N, S, M))