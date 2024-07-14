"""# N types  candies

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
"""

import math

def min_cost_to_buy_all_candies(N, K, candies):
    # Sort the candies by their prices in ascending order
    candies.sort()
    
    # Calculate the number of candies we need to actually buy
    num_candies_to_buy = math.ceil(N / (K + 1))
    
    # Calculate the minimum cost by summing the prices of the cheapest candies
    min_cost = sum(candies[:num_candies_to_buy])
    
    return min_cost

# Example 1
N = 4
K = 2
candies = [3, 2, 1, 4]
print(min_cost_to_buy_all_candies(N, K, candies))  # Output: 3

# Example 2
N = 5
K = 4
candies = [3, 2, 1, 4, 5]
print(min_cost_to_buy_all_candies(N, K, candies))  # Output: 1
