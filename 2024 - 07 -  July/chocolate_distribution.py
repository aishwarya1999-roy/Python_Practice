def chocolate(arr,N,M):
    for i in range(len(arr)-2):
        sorted(arr)
        print(arr[i],arr[i+1],arr[i+2])

    return sorted(arr)

arr = [3, 4, 1, 9, 56, 7, 9, 12] #[1, 3, 4, 7, 9, 9, 12, 56]
N = 8
M = 5

print(chocolate(arr,N,M))