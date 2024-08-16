#array is sorted or not
def sorted_or_not(arr):
    if len(arr)==1 or len(arr)==0:
        return True
    if arr[0]>arr[1]:
        return False
    """if arr[i]>arr[i-1]:
        return True"""
    return sorted_or_not(arr)
arr = [1,3,5,7,8]
print(sorted_or_not(arr))