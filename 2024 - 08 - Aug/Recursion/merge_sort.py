def merge_sort(arr, n,s,e):
    if s>e:
        return
    mid = (s+e)//2
    print(arr[mid])
    left = merge_sort(arr,n-1,s,mid+1)
    right = merge_sort(arr,n-1,mid+1,e)
    print("left: ", left)
    print("right: ", right)
    

arr = [55, 16, 9, 23, 3, 12, 3]
    #   0   1  2  3   4   5  6
merge_sort(arr, 7,0,7)
