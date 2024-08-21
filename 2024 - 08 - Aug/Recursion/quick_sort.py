def partition(arr,low,high):
    pivot = arr[low]
    i = low +1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        j = partition(arr,low,high)
        quick_sort(arr,low,j-1)
        quick_sort(arr,j+1,high)

arr = [4,6,1,9,5,2]
quick_sort(arr,0,len(arr)-1)
print("Sorted array:", arr)
