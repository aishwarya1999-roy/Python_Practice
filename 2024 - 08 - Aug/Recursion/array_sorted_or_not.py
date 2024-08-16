#array is sorted or not
def sorted_or_not(i,arr):
    
    if len(arr)<1:
        return 
    if arr[i]>arr[i-1]:
        return True
    sorted_or_not(i+1,arr)
arr = [1,3,5,7,8]
i = 0
print(sorted_or_not(i, arr))