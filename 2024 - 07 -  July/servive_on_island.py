import math

def minfood(N, S, M):
    food = 0
    food = math.ceil((M*S)/N)
    if food >= S-1:
        return -1
    return food

N = 16 # max food you can buy each day
S = 10 # days to servive
M = 2 # unit of food each day to eat
print(minfood(N, S, M))