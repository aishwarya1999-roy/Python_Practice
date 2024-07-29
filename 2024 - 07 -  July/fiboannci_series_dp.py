import timeit

#recusive
def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

#dynamic recursive
def fibo_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
    return memo[n]

# dynamic iterative = time O(n), space = O(n)
def fibo_iter(n):
    dp = [0] * (n + 1)
    if n<=1:
        return n
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i]=dp[i-2] + dp[i-1]

    return dp[n]


# Space Optimization: = time O(n), space = O(1)
def fibo_space_op(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1



"""
# Time the plain recursive function
recursive_time = timeit.timeit('fibo_recursive(5)', globals=globals(), number=1)  # number=1 for plain recursive due to high time
print(f"Plain recursive time: {recursive_time} seconds")
"""

# Time the memoized function
memoized_time = timeit.timeit('fibo_memo(50)', globals=globals(), number=1)  # number=1 for memoized function
print(f"Memoized time: {memoized_time} seconds")
print("memoized function : ", fibo_memo(50))

# Time the iterative function
memoized_time = timeit.timeit('fibo_iter(50)', globals=globals(), number=1)  # number=1 for memoized function
print(f"Memoized time: {memoized_time} seconds")
print("iterative function : ", fibo_iter(50))


print("space_optimization : " , fibo_space_op(50))