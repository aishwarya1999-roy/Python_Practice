import math

def minfood(N, S, M):
    sunday = S//7
    food = math.ceil((M*S)/N)
    
    return food

N = 2 # max food you can buy each day
S = 5 # days to servive
M = 2  # unit of food each day to eat
print(minfood(N, S, M))