# decimal_to_binary
"""def decimal_to_binary(x):
    res = ""
    while x > 0:
        if x%2 == 1:
            res+="1"
        else:
            res+="0"
        x//=2
    return res[::-1]
x = 15
print(decimal_to_binary(x))"""


# binary_to_decimal

"""def binary_to_decimal(binary_str):
    decimal_value = 0
    for i, digit in enumerate (reversed (binary_str)):
        if digit == '1':
            decimal_value += 2 ** i
    return decimal_value
binary_string = "101"
print(binary_to_decimal(binary_string))"""

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

# Three Consecutive Odds

arr =[1,2,3,5,7,6,7]
n = len(arr)
for i in range(0,n):
    if arr[i]%2 != 0 and arr[(i+1)]%2 != 0 and arr[(i+2)]%2 != 0:
        print(arr[i],arr[i+1],arr[i+2])
    else:
        continue