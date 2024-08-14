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
"""def counting(num):
    if num == 0:
        return 0
    print(num)
    return counting(num-1)
    
num = int(input("Number : "))
print(counting(num))
"""

#fibo

"""def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
     
    return fibonacci(n-1)+fibonacci(n-2)

n = int(input())
print(fibonacci(n))"""

#reaching home - level 0 recursion
"""def power_function(dest, sour):
    print("Source : ", sour, "Destination : ", dest)
    if sour == dest:
        return "Reached Home"
    
    return power_function(dest, sour+1)

dest = int(input("Destination : "))
sour = int(input("Source : "))
print(power_function(dest, sour))"""


#stair climbing
def power_function(dest, sour):
    count = 0
    print("Source : ", sour, "Destination : ", dest)
    if sour == dest:
        return "Reached Destination"
    
    count+=1
    return power_function(dest, sour+2)

dest = int(input("Destination : "))
sour = 0
print(power_function(dest, sour))