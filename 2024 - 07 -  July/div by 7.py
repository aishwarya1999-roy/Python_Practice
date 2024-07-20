def minimum_buying_days(N, S, M):
    # Calculate total food required for S days
    total_food_required = S * M
    # Calculate the number of Sundays
    sundays = S // 7
    # Calculate the number of available buying days
    buying_day = S - sundays
    
    # Calculate minimum buying days required
    if total_food_required % N == 0:
        min_buying_days = total_food_required // N
    else:
        min_buying_days = total_food_required / N + 1 
    
    # Check if the minimum buying days is within the available buying days
    if min_buying_days > buying_day:
        return -1
    else:
        return min_buying_days

N = 9
S = 10
M = 8

print(minimum_buying_days(N, S, M))
