# N types  candies

def candy_shop(N, price, K):
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
N = 5
price = [3,2,1,4, 5] # 1, 2, 3, 4
K = 4
print(candy_shop(N, sorted(price), K))