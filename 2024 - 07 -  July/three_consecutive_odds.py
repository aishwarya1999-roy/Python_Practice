
# Three Consecutive Odds
#approch 1 - Using a For Loop with Indexing
"""arr = [1, 2, 3, 4, 3, 9, 7, 4, 5,7,9]
n = len(arr)

for i in range(n - 2):  # Adjust the loop to stop at n-2
    if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
        print(arr[i], arr[i + 1], arr[i + 2])"""

#approch 2 - Using a Counter
def three_consecutive_odds(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

# Example usage:
arr = [2, 6, 4, 1, 3, 5]
print(three_consecutive_odds(arr))
