def bubble_sort(arr, n):
    if n == 0 or n == 1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]= arr[i], arr[i+1]
    return bubble_sort(arr, n-1)

arr = [5,1,9,2,3]
n = len(arr)
print(bubble_sort(arr, n))