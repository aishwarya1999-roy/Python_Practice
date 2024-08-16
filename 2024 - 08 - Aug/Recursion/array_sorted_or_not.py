#array is sorted or not
def sorted_or_not(i,arr):
    if len(arr):
        return 
    return sorted_or_not(i+1, arr)

arr = [4,5,7,8,3]
i = 0
print(sorted_or_not(i, arr))