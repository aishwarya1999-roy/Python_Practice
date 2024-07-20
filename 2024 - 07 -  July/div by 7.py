def minimum_buying_days(N, S, M):
    total_food_required = S * M
    sunday= S // 7
    if M > N:
        return -1
    min_buying_days = (total_food_required + N - 1) // N
    if min_buying_days > S-sunday:
        return -1
    
    return min_buying_days

# Example usage:
N = 16  # Max food Geekina can buy each day
S = 10  # Number of days Geekina needs to survive
M = 2   # Food Geekina needs each day

print(minimum_buying_days(N, S, M))  # Should return the minimum number of days needed to buy food or -1 if not possible
