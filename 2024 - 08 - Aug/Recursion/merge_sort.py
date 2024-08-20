def merge_sort(arr, n,s,e):
    if n ==1:
        return
    mid = (s+e)//2
    print(arr[mid])
    left = arr[s:mid+1]
    right = arr[mid+1:e]
    print("left: ", left)
    print("right: ", right)
    return merge_sort(left,n-1,s,mid)

arr = [55, 16, 9, 23, 3, 12, 3]
    #   0   1  2  3   4   5  6
merge_sort(arr, 7,0,7)
