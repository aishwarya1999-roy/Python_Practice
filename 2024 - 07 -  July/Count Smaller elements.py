def smaller_count(arr):
    
    new_ar = []
    N = len(arr)
    count = 0
    for i in range(0,N-1):
        
        for j in range(i+1, N-1):
            if j < i :
                count+=1
            new_ar.append(count)


    return new_ar
arr = [12, 1, 2, 3, 0, 11, 4]
print(smaller_count(arr))
