def merge_sort(arr, n,s,e):
    if n ==0:
        return
    mid = (s+e)//2
    left = merge_sort(arr,n-1,s,mid)
    right = merge_sort(arr,n-1,mid+1,e)
    print(left)

arr = [55, 16, 9, 23, 3, 12, 3]
    #   0   1  2  3   4   5  6
n = 7
s= 0
e = 6
merge_sort(arr, n,s,e)
