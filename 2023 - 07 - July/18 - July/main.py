# ARRAY
# Two Sum: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

array = [8, 2, 7, 5, 1]

inp = int(input("Enter the target : "))
arr = sorted(array)[::-1]
f = 0
def twosum():

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == inp:
                return [i, j]
            else:
                f = 1
                return f

print(f)
"""if f == 1:
    print(f"Please Enter target till max {arr[0]+arr[1]}")
else:
    print(twosum())"""
