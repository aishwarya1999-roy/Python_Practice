def merge(arr,mid,s,e):
    left = arr[s:mid+1]
    right = arr[mid+1:e+1]
    i= j = 0
    k = s
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
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
    print(arr[i], end=" ")