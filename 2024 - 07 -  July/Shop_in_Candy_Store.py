# N types  candies

"""def candy_shop(N, price, K):
    max_money = 0
    min_money = 0
    i=0
    while len(price)>1:
        print("Before : ",i, price)
        min_money += price[i]
        [price.pop() for i in range(K) if len(price)>1]
        print("After : " , price)
        i+=1
    return min_money
N = int(input("Enter amount for N : "))
K = int(input("Enter amount for K : "))
price = [3,2,1,4] # 1, 2, 3, 4
price = list(map(int, input()) for i in range(N))

print(candy_shop(N, sorted(price), K))"""

N = int(input("Enter amount for N : "))
price = list(map(int, input()))
print(price)