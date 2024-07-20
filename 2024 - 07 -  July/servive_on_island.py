def minfood(N, S, M):
    food = 0
    if M>N:
        return -1
    else:
        food = math.celi((M*S)//N)
    return food

N = 16 # max food you can buy each day
S = 10 # days to servive
M = 2 # unit of food each day to eat
print(minfood(N, S, M))