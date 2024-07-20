import math

def minfood(N, S, M):
    weeks = S//7
    extra_days = S%7
    max_buy_day = weeks * 6 + extra_days
    if M>N:
        return -1
    
    food =(M*S + N-1)//N


N = 2 # max food you can buy each day
S = 5 # days to servive
M = 2  # unit of food each day to eat
print(minfood(N, S, M))