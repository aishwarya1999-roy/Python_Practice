def minimum_buying_days(N, S, M):
    sunday = S//7
    total_food = S * M
    buying_day = S - sunday
    food = -1
    if total_food % N == 0:
        food = total_food//N
    else:
        food = (total_food//N) + 1
    if buying_day<food:
        return -1
    else:
        return food

print(minimum_buying_days(9, 10, 8))
print(minimum_buying_days(2, 5, 2))
print(minimum_buying_days(24, 35, 20))
