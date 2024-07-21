def chocolate(arr,N,M):
    arr.sort()
    i = 0
    j = M-1
    mini = float('inf')
    while j<N:
        diff = arr[j] - arr[i]
        mini.append(diff)
        i+=1
        j+=1
    return min(mini)

arr = [3, 4, 1, 9, 56, 7, 9, 12] #[1, 3, 4, 7, 9, 9, 12, 56]
N = 8
M = 5

print(chocolate(arr,N,M))