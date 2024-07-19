def smaller_count(arr):
    
    new_ar = []
    N = len(arr)
    for i in range(0,N):
        count = 0
        for j in range(i+1, N):
            if arr[j] < arr[i] :
                count+=1
        new_ar.append(count)


    return new_ar
arr = [12, 1, 2, 3, 0, 11, 4]
print(smaller_count(arr))
