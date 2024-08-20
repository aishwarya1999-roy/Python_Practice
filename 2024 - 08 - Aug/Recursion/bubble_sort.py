def bubble_sort(arr, n):
    
    if n == 0 or n == 1:
        return
    for i in range(n-1):
        print("n : ", n)
        print("arr[i] : ", arr[i], "arr[i+1] : " , arr[i+1])
        if arr[i]>arr[i+1]:
            print("yes")
            arr[i],arr[i+1]==arr[i], arr[i+1]
        i=i+1
    bubble_sort(arr, n-1)
arr = [5,1,9,2,3]
n = len(arr)
bubble_sort(arr, n)

# for i in range(n):
#     print(arr[i], end=" ")
