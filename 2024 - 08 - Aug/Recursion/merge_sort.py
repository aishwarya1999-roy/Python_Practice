def merge(arr,mid,s,e):
    left = arr[s:mid+1]
    right = arr[mid+1:e+1]
    i= j = 0
    k = s

def merge_sort(arr, s,e):
    if s>=e:
        return
    mid = (s+e)//2
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    merge(arr,mid,s,e)

arr = [55, 16, 9, 23, 1, 12, 3]
n = len(arr)
merge_sort(arr, 0,n-1)

for i in range(n):
    print(arr[i])