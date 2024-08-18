def binary_search(arr,search,l,h):
    mid = (l+h)//2
    if l>h:
        return -1
    if arr[mid] == search:
        return mid
    if arr[mid]>search:
        return binary_search(arr,search,l,mid-1)
    elif arr[mid]<search:
        return binary_search(arr,search,mid+1,h)
arr = [1,4,8,15,20]
search = 5
l = 0
h = len(arr)
print(binary_search(arr,search,l,h))


