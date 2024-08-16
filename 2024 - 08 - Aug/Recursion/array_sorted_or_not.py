#array is sorted or not
def sorted_or_not(arr,n):
    if n==1 or n==0:
        return True
    if arr[0]>arr[1]:
        return False
    else:
        ans = sorted_or_not(arr[1:],n-1)
        return ans
arr = [1,3,6,7,8]
n = len(arr)
ans = sorted_or_not(arr,n)
if ans is True:
    print("Array is sorted")
else:
    print("Array is not sorted")