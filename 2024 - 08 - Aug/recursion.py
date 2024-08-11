def fact(N):
    if N == 0:
        return
    return N * fact(N-1)

N = 5
print(fact(N))