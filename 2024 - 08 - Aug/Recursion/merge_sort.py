def merge_sort(arr, n,s,e):
    if s>e:
        return
    mid = (s+e)//2
    print(arr[mid])
    merge_sort(arr,n-1,s,mid+1)
    merge_sort(arr,n-1,mid+1,e)

arr = [55, 16, 9, 23, 3, 12, 3]
    #   0   1  2  3   4   5  6
n = len(arr)
merge_sort(arr, 0,n-1)
