def chocolate(arr,N,M):
    for i in range(N-2):
        arr.sort()
        new_arr = []
        mini = min(arr[i],arr[i+1],arr[i+2])
        maxi = max(arr[i],arr[i+1],arr[i+2])
        print("min :" , mini, end=", ")
        print("max :" ,maxi, end=", ")
        new_arr.append(maxi-mini)
        print(min(new_arr))
    return arr

arr = [7, 3, 2, 4, 9, 12, 56] #[1, 3, 4, 7, 9, 9, 12, 56]
N = 7
M = 3

print(chocolate(arr,N,M))