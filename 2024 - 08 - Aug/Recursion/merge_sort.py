def merge_sort(arr, n):
    if n == 0 or n == 1:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1], arr[i] 
    merge_sort(arr, n-1)

arr = [55,16,9,23,3,12,3]
n = len(arr)
merge_sort(arr, n)
for i in range(n):
    print(arr[i], end=" ")
