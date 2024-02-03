"""list1 = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
l = 0
h = len(list1)
key = int(input("Search element : "))
val = 0
while l<=h:
    mid = int((l + h) / 2)
    if key == list1[mid]:
        val = 1
        break
    elif key < list1[mid] :
        h = mid- 1
    else :
        l = mid + 1
if val == 1:
    print(f"Search element {key} Found at position {mid}")
else:
    print(f"Search element {key} is not in the List")"""

# -------------- Iterative method --------------
# time complexity = O(logn)
"""def binary_search(arr, n, key):
    l = 0
    h = n
    while l <= h:            #---- 1
        mid = int((l + h) / 2)
        if key == arr[mid]:       # ---- 1
            return mid
        elif key < arr[mid]:    # ---- 1
            h = mid - 1
        else:
            l = mid + 1             # exit loop ------  O(log n) 
    return -1
    
array = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
n = len(array)-1
key = int(input("Search element : "))
pos = binary_search(array, n, key)
if pos == -1:
    print("Not found")
else:
    print(f"Search element {key} Found at { pos + 1}")"""

# in each loop , it is diving the list into half, so it became, n/2, n/2^2, n/2^3, ..... , n/2^k , so it will continue till 1,
# so assume, n/2^k = 1, 2^k = n, k = log n
# so, t(n) = O(log n)


# ----------- recursive method --------------
# time complexity = O(logn)
"""def binary_search(arr,l,h,key):
    if l <= h:
        mid = (l + h) // 2
        if arr[mid] == key:    # ---- 1
            return mid
        elif key < arr[mid]: 
            return binary_search(arr, l, mid - 1, key)  #---- t(n/2)
        else:
            return binary_search(arr, mid + 1, h, key)
    else:
        return -1

arr = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
l, h = 0, len(arr)-1
key = int(input("Search element : "))
pos = binary_search(arr,l, h, key)
if pos == -1:
    print("Not found")
else:
    print(f"Search element {key} Found at position {pos}")"""

"""T(n) = T(n/2) + 1
so, t(n) = O(n^0 log n)
         =  O(log n)"""