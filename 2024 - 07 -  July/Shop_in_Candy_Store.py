# N types  candies

def candy_shop(N, price, K):
    max_money = 0
    min_money = 0
    for j in range(0,len(price)):
        print("Before : " , price)
        min_money += price[j]
        [price.pop() for i in range(K)]
        print("After : " , price)
    return min_money





N = 4
price = [3,2,1,4,6] # 1, 2, 3, 4, 6
K = 2
print(candy_shop(N, sorted(price), K))