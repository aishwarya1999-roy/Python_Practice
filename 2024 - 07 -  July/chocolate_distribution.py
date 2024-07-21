def chocolate(arr,N,M):
    arr.sort()
    i = 0
    j = M-1

    while j<N:
        diff = arr[i] - arr[j]
        print(diff)
        i+=1
        j+=1
    return arr

arr = [7, 3, 2, 4, 9, 12, 56] #[1, 3, 4, 7, 9, 9, 12, 56]
N = 7
M = 3

print(chocolate(arr,N,M))