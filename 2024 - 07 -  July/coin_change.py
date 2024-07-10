def coin_change(n, arr):
    arr.sort(reverse=True)
    remaining_amount = n
    total_coins = 0
    coins_used = {denom: 0 for denom in arr}
    print("Amount to be given", n)
    print(arr)
    while remaining_amount > 0:
        for coin in arr:
            if remaining_amount >= coin:
                print("Coin chosen", coin)
                remaining_amount -= coin 
                total_coins += 1
                coins_used[coin] += 1
                print("Amount remaining", remaining_amount)
                break
    for coin, count in coins_used.items():
        for _ in range(count):
            print(coin)

target_amount = 15
denominations = [1, 3, 5, 10]
coin_change(target_amount, denominations)
