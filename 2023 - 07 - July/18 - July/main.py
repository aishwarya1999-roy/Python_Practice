# ARRAY
# Two Sum: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

array = [8, 2, 7, 5, 1]
inp = int(input("Enter the target : "))
arr = sorted(array)[::-1]
def twosum():
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == inp:
                return [i, j]
            else:
                print("Error")
print(twosum())
