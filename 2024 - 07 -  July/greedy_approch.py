# finding min or max

"""Greedy approach is good when the problem size is large and 
attempts at arriving at the best solution will end up being more 
costly than arriving at an acceptable optimal solution"""

#coin cahnge problem

def coin_change(arr,n):
    arr.sort(reverse=True)
    rem = n
    coun = 0
    coins_used = {denom: 0 for denom in arr}
    for i in arr:
        while rem >= i:
            rem = rem-i
            coun +=1
            coins_used[i]+=1
    print("Minimum number of coins needed:", coun)
    for coin, count in coins_used.items():
        if count > 0:
            print(f"{count} coin(s) of {coin}$")

arr = [1,2,5,6]
n = 8
coin_change(arr,n)
