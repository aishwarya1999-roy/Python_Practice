def minimum_buying_days(N, S, M):
    total_food_required = S * M
    sunday= S // 7
    buying_day = S - sunday
    min_buying_days = 0

    if total_food_required % N ==0:
        min_buying_days = total_food_required//N
    else:
        min_buying_days = total_food_required//N + 1 
    
    if min_buying_days <= buying_day:
        return min_buying_days
    else:
        return -1

N = 9
S = 10
M = 8

print(minimum_buying_days(N, S, M))

int M = 8,N = 9,S = 10;
int sunday = S/7;
int total_food_required = S * M;
int buying_day = S - sunday
int min_buying_days = 0

if(total_food_required % N) == 0 {
    min_buying_days = total_food_required/N
}
else{
    min_buying_days = total_food_required/N + 1
}
if(min_buying_days <= buying_day)
    return min_buying_days;
else
    return -1;

print(min_buying_days)