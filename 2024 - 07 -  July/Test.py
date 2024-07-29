# A cab service offers three types of passes. 1D, 7D, 30D. A T days pass can be used for a continuous duration only. 
# Consider the days of the year being labeled sequentially from 1 to 365.
# Travelling is required only on some selected days of the year(input). 
# Given the cost of different passes and the days on which travel is required, 
# Calculate the minimum amount using which we can travel on all these days.


# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11(2 + 7 + 2)

def get_min(days, cost):
    mini = float('inf')
    
    
days = [1,4,6,7,8,20]
cost = [2, 7, 15]