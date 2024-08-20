def merge(arr,s,e):
    mid=(s+e)//2
    size1= mid-s+1
    size2 = e-mid
    left = []
    right= []
    k = s
    for i in range(size1):
        left.append[k]
    return

def merge_sort(arr, s,e):
    if s>=e:
        return
    mid = (s+e)//2
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    merge(arr,s,e)

arr = [55, 16, 9, 23, 1, 12, 3]
n = len(arr)
merge_sort(arr, 0,n-1)
