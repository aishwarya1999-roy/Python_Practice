def minimum_buying_days(N, S, M):
    total_food_required = S * M
    weeks = S // 7
    extra_days = S % 7
    max_buying_days = weeks * 6 + extra_days
    if M > N:
        return -1
    min_buying_days = (total_food_required) / N
    print(min_buying_days)
    if min_buying_days > max_buying_days:
        return -1
    
    return min_buying_days


N = 9
S = 10
M = 8

print(minimum_buying_days(N, S, M)) 