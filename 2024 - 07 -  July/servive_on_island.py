import math

def minfood(N, S, M):
    for i in range(1, S):
        if i%7 == 0:
            sunday+=1
    sun = 1
    food = math.ceil((M*S)/N)
    if food >= S-sun:
        return -1
    return food

N = 9 # max food you can buy each day
S = 10 # days to servive
M = 8 # unit of food each day to eat
print(minfood(N, S, M))