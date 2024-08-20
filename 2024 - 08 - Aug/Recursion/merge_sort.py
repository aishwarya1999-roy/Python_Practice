def merge_sort(arr, n,s,e):
    if n ==0:
        return
    mid = (s+e)//2
    print(mid)
    left = arr[s:mid+1]
    print(left)

arr = [55, 16, 9, 23, 3, 12, 3]
    #   0   1  2  3   4   5  6
merge_sort(arr, 7,0,7)
