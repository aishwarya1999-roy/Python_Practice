# Memoization Implementation:
def dp_function_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = dp_function_memo(n-1) + dp_function_memo(n-2)
    return memo[n]

#Tabulation Implementation:
def dp_function_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(dp_function_tab(7))