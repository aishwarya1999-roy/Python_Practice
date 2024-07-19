def candy_shop(N, price, K):
    price.sort()
    mini = 0
    buy = 0
    free = N - 1
    while buy <= free:
        mini = mini + price[buy]
        buy += 1
        free = free - K

    maxi = 0
    buy = N-1
    free = 0

    while free <= buy:
        maxi = maxi + price[buy]
        buy-=1
        free+=K

    return mini, maxi
N = 4
K = 2
price = [3,2,1,4] # 1 2 3 4

print(candy_shop(N, price, K))