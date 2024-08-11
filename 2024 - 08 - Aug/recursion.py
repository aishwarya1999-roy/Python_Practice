# factorial - recursion
def fact(N):
    print("N : ", N)
    if N == 0:
        return 1
    return N * fact(N-1)
N = 5
print(fact(N))