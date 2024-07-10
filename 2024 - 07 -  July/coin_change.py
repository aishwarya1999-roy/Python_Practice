def coin_change(target_amount, denominations):
    # Sort the denominations in descending order
    denominations.sort(reverse=True)
    
    # Initialize variables
    remaining_amount = target_amount  # The amount that still needs to be given
    total_coins = 0  # Total number of coins used
    coins_used = {denom: 0 for denom in denominations}  # Dictionary to track the count of each denomination
    
    # Print the initial amount to be given
    print("Amount to be given", target_amount)
    print(denominations)  # Print the sorted denominations
    
    # Greedy algorithm to determine the minimum number of coins
    while remaining_amount > 0:
        for coin in denominations:
            if remaining_amount >= coin:
                # Choose the coin
                print("Coin chosen", coin)
                remaining_amount -= coin  # Subtract the coin's value from the remaining amount
                total_coins += 1  # Increment the total coin count
                coins_used[coin] += 1  # Increment the count for this denomination in the dictionary
                
                # Print the remaining amount after choosing the coin
                print("Amount remaining", remaining_amount)
                
                # Break the loop to start again with the largest coin
                break
    
    # Print the results
    for coin, count in coins_used.items():
        for _ in range(count):
            print(coin)

# Example usage
target_amount = 8
denominations = [1, 3, 5, 6]
coin_change(target_amount, denominations)
