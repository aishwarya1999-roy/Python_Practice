def smaller_count(arr):
    
    new_ar = []
    N = len(arr)
    for i in range(0,N-1):
        count = 0
        for j in range(i+1, N-1):
            if arr[j] < arr[i] :
                count+=1
        new_ar.append(count)


    return new_ar
arr = [12, 1, 2, 3, 0, 11, 4]
print(smaller_count(arr))
