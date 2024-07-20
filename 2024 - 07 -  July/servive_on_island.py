import math

def minfood(N, S, M):
    sunday = S//7
    food = math.ceil((M*S)/N)
    if food >= S-sunday:
        return -1
    return food

N = 9 # max food you can buy each day
S = 10 # days to servive
M = 8 # unit of food each day to eat
print(minfood(N, S, M))