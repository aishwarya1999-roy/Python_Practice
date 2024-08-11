# factorial - recursion
def fact(N):
    if N == 0:
        return 1
    return N * fact(N-1)
N = input()
print(fact(N))