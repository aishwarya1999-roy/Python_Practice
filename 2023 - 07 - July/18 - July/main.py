# ARRAY
# Two Sum: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

array = [1,2,3,5,8]
inp = 3
def twosum():
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == inp:
                return [i,j]
print(twosum())


