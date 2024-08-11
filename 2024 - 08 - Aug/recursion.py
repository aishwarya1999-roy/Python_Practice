# factorial - recursion
"""def fact(N):
    if N == 0:
        return 1
    return N * fact(N-1)
N = int(input("N : "))
print(fact(N))"""

#power - recursion
"""def power_function(num, power):
    if power == 0:
        return 1
    return num * power_function(num, power-1)
num = int(input("Number : "))
power = int(input("power : "))
print(power_function(num, power))"""

#counting - recursion
def power_function(num, power):
    if power == 0:
        return 1
    return num * power_function(num, power-1)
num = int(input("Number : "))
print(power_function(num))
