# N types  candies

def candy_shop(N, price, K):
    price.sort()
    min_money = 0
    i=0
    while i<N:
        min_money += price[i]
        [price.pop() for i in range(K)]
        i += 1
    return min_money
N = int(input("Enter amount for N : "))
K = int(input("Enter amount for K : "))
price = [int(input("Enter Element for candy : ")) for i in range(N)]

print(candy_shop(N, price, K))