def minimum_buying_days(N, S, M):
    total_food_required = S * M
    sunday= S // 7
    buying_day = S - sunday
    
    if M > N:
        return -1
    min_buying_days = (total_food_required + N - 1) // N
    
    if min_buying_days >= buying_day:
        return -1
    else:
        return min_buying_days

# Example usage:
N = 2  # Max food Geekina can buy each day
S = 5  # Number of days Geekina needs to survive
M = 2  # Food Geekina needs each day

print(minimum_buying_days(N, S, M))  # Should return the minimum number of days needed to buy food or -1 if not possible
