def linear_search(arr,search,n):
    if n == 0:
        return False
    if arr[0] == search:
        return True
    else:
        return linear_search(arr[1:], search,n-1)
arr = [3,5,1,2,6]
search = 2
n= len(arr)
ans = linear_search(arr,search,n)
if ans is True:
    print("Present")
else:
    print("Not Present")