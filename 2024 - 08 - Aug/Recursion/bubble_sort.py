def bubble_sort(arr, n):
    print(arr)
    if n == 0 or n == 1:
        return
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]= arr[i], arr[i+1]
        i=i+1
    bubble_sort(arr, n-1)
    print(arr)

arr = [5,1,9,2,3]
n = len(arr)
print(bubble_sort(arr, n))