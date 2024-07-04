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
n = 12

