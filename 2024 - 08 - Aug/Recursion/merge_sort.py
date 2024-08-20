def merge_sort(arr, n,s,e):
    if n ==0:
        return
    mid = (s+e)//2
    left = merge_sort(arr,n,s,mid)
    right = merge_sort(arr,n,mid+1,e)
    print(left,right)
    return 

arr = [55, 16, 9, 23, 3, 12, 3]
    #   0   1  2  3   4   5  6
n = len(arr)
s= 0
e = len(arr)-1
print(merge_sort(arr, n,s,e))
