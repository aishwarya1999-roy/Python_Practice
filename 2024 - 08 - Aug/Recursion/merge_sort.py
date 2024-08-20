def merge_sort(arr, n,s,e):
    mid = (s+e)//2
    print(arr[mid])
    return merge_sort(arr, n,s,e)

arr = [55,16,9,23,3,12,3]
n = len(arr)
s= 0
e = len(arr)-1
print(merge_sort(arr, n,s,e))
