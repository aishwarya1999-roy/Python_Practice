import timeit

def fibo_recursive(n):
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
    return memo[n]

# Time the plain recursive function
recursive_time = timeit.timeit('fibo_recursive(18)', globals=globals(), number=1)  # number=1 for plain recursive due to high time
print(f"Plain recursive time: {recursive_time} seconds")

# Time the memoized function
memoized_time = timeit.timeit('fibo_memo(900)', globals=globals(), number=1)  # number=1 for memoized function
print(f"Memoized time: {memoized_time} seconds")
