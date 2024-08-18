#power - recursion - way 1
# def power_function(num, power):
#     if power == 0:
#         return 1
#     if power == 1:
#         return num
#     return num * power_function(num, power-1)
# num = int(input("Number : "))
# power = int(input("power : "))
# print(power_function(num, power))

#power - recursion - way2
def power_function(num, power):
    if power == 0:
        return 1
    if power == 1:
        return num
    ans = power_function(num, power//2)
    if power%2==0:
        return ans * ans
    else:
        return num * ans * ans
num = int(input("Number : "))
power = int(input("power : "))
print(power_function(num, power))