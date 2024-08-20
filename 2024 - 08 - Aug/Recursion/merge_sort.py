def merge_sort(arr, s,e):

    if s==e:
        print(arr[s:e+1])
        return
    mid = (s+e)//2

    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    

arr = [55, 16, 9, 23, 1, 12, 3]
    #   0   1  2  3   4   5  6
n = len(arr)
merge_sort(arr, 0,n-1)
