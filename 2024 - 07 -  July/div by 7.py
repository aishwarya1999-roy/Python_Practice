def minimum_buying_days(N, S, M):
    total_food = S*M
    if N < M:
        return -1
    if (N-M)*6 < M and S > 6:
        return -1
    if total_food%N == 0 and N == M and S > 6:
        food = -1

    elif total_food%N == 0:
        food = total_food//N
    else:
        food = total_food//N + 1
    return food

print(minimum_buying_days(9, 10, 8))
print(minimum_buying_days(2, 5, 2))
print(minimum_buying_days(24, 35, 20))
