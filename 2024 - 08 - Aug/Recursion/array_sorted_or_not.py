#array is sorted or not
def sorted_or_not(i,arr):
    if i>=len(arr):
        return 
    if arr[i]>arr[i-1]:
        print("sorted")
    return sorted_or_not(i+1,arr)

arr = [3,4,5,7,8]
i = 0
sorted_or_not(i, arr)