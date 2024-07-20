def minimum_buying_days(N, S, M):
    # Total food required
    total_food_required = S * M
    
    # Number of weeks and extra days
    weeks = S // 7
    extra_days = S % 7
    
    # Maximum days you can buy food
    max_buying_days = weeks * 6 + extra_days
    
    # Check if it's possible to survive
    if M > N:
        return -1  # Impossible to survive since daily requirement is more than daily buying limit
    
    # Minimum buying days needed
    min_buying_days = (total_food_required + N - 1) // N  # This is ceil(total_food_required / N)
    
    # Check if the minimum buying days is within the maximum buying days
    if min_buying_days > max_buying_days:
        return -1  # Impossible to survive since we can't buy enough food in available days
    
    return min_buying_days

# Example usage:
N = 16  # Max food Geekina can buy each day
S = 10  # Number of days Geekina needs to survive
M = 2   # Food Geekina needs each day

print(minimum_buying_days(N, S, M))  # Should return the minimum number of days needed to buy food or -1 if not possible
