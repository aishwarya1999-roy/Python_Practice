
#brute force

"""def smaller_count(arr):
    
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
print(smaller_count(arr))"""

#opsimized

def merge_count_smaller(arr, indices, start, end, result):
    if end - start <= 1:
        return
    
    mid = (start + end) // 2
    merge_count_smaller(arr, indices, start, mid, result)
    merge_count_smaller(arr, indices, mid, end, result)
    
    temp = []
    right_counter = 0
    i, j = start, mid
    
    while i < mid and j < end:
        if arr[indices[j]] < arr[indices[i]]:
            temp.append(indices[j])
            right_counter += 1
            j += 1
        else:
            temp.append(indices[i])
            result[indices[i]] += right_counter
            i += 1
    
    while i < mid:
        temp.append(indices[i])
        result[indices[i]] += right_counter
        i += 1
    
    while j < end:
        temp.append(indices[j])
        j += 1
    
    for i in range(len(temp)):
        indices[start + i] = temp[i]

def count_smaller(arr):
    N = len(arr)
    result = [0] * N
    indices = list(range(N))
    merge_count_smaller(arr, indices, 0, N, result)
    return result

arr = [12, 1, 2, 3, 0, 11, 4]
print(count_smaller(arr))
