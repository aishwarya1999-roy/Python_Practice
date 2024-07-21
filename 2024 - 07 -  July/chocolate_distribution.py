def chocolate(arr,N,M):
    for i in range(len(arr)-2):
        arr.sort()
        mini = min(arr[i],arr[i+1],arr[i+2],)
        maxi = max(arr[i],arr[i+1],arr[i+2])
        print("min :" , mini, end=", ")
        print("max :" ,maxi, end=", ")
        print("max - min:" , maxi-mini)
    return arr

arr = [7, 3, 2, 4, 9, 12, 56] #[1, 3, 4, 7, 9, 9, 12, 56]
N = 8
M = 5

print(chocolate(arr,N,M))