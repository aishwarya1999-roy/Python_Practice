# Swap two numbers without using third variable
"""a = 5
b = 6
a = a^b
b=a^b
a=a^b
print(a,b)
"""


#check if the ith bit is set or not using << 
"""n = 13
i = 2
if (n & (1<<i)) != 0:
    print("Set")
else:
    print("unset")"""

#check if the ith bit is set or not using << 
"""n = 13
i = 1
if ((n >> i) & 1) != 0:
    print("Set")
else:
    print("unset")"""

#set the ith bit
"""n = 9
i = 2
print(n|(1<<i))"""

#clear the set in ith bit
"""n = 9
i = 2
print(n& ~(1<<i))"""

#toggle the ith bit

#print(n^(1<<i))


#remove the last set bit
"""N = 12
print(N&(N-1))"""

#check number is power of 2 or not
"""N = 18
if (N&(N-1)) == 0:
    print("power of 2")
else:
    print("not")"""

#count num of set bit

#way 1 - brute force
"""def count_set(n):
    count = 0
    while n>1:
        if n%2==1:
            count+=1
            
        n=n//2
    if n == 1:
        count += 1
    
    return count

n = 30
print(count_set(n))"""

#way 2 - bitwis
"""def count_set(n):
    count = 0
    while n>1:
        count+=n&1
        n=n>>1
    if n == 1:
        count+=n&1
    return count
n = 84
print(count_set(n))"""

#way 3 - bitwis
"""def count_set(n):
    count = 0
    while n!= 0:
        n = n & (n-1)
        count+=1

    return count
n = 84
print(count_set(n))

"""
#odd even using bitwise opearators
"""n = 16
if n&1 == 1:
    print("Odd")
else:
    print("even")"""


