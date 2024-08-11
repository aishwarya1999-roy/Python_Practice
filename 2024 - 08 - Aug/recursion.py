# factorial - recursion
"""def fact(N):
    if N == 0:
        return 1
    return N * fact(N-1)
N = int(input("N : "))
print(fact(N))"""

#power - recursion
def power_function(N):
    if N == 0:
        return 1
    return N * power(N-1)
num = int(input("N : "))
power = int(input("power : "))
print(power_function(num, power))