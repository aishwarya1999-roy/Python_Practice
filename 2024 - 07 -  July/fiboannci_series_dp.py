def fibo(n):
    if n<=1:
        return n
    return fibo(n-2) + fibo(n-1)
n = 10
print(fibo(n))