# N types  candies

def candy_shop(N, price, K):
    max_money = 0
    min_money = 0
    for i in range(0,len(price)-1):
        min_money += price[i]
        [price.pop() for i in range(K)]

    return min_money





N = 4
price = [3,2,1,4,6] # 1, 2, 3, 4, 6
K = 2
print(candy_shop(N, sorted(price), K))