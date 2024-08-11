def fact(N):
    print("N : ", N)
    if N == 0:
        return N
    return N * fact(N-1)

N = 5
print(fact(N))