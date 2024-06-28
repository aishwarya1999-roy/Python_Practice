def max_profit(N, profit, price):
    dp = [-float('inf')] * (1 << N)
    dp[0] = 0
    for mask in range(1 << N):
        for i in range(N):
            if not (mask & (1 << i)):
                new_mask = mask | (1 << i)
                additional_profit = -price[i]
                for j in range(N):
                    if mask & (1 << j):
                        additional_profit += profit[i][j]
                dp[new_mask] = max(dp[new_mask], dp[mask] + additional_profit)

    max_profit = -float('inf')
    for mask in range(1 << N):
        current_profit = dp[mask]
        for i in range(N):
            for j in range(i + 1, N):
                if not (mask & (1 << i)) and not (mask & (1 << j)):
                    current_profit -= profit[i][j]
        max_profit = max(max_profit, current_profit)
    
    return max_profit

N = int(input().strip())
profit = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    profit.append(row)
price = []
for _ in range(N):
    price.append(int(input().strip()))
print(f"Maximum Profit: {max_profit(N, profit, price)}")

