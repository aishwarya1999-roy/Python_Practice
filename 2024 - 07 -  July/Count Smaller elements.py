def smaller_count(arr):
    count = 0
    new_ar = []
    N = len(arr)
    for i in range(0,N-1):
        for j in range(i+1, N-1):
            if j < i :
                count+=1
        new_ar.append(count)


    return new_ar
arr = [12, 1, 2, 3, 0, 11, 4]
print(smaller_count(arr))

12  count = 0
1   count = 0+1
2   count = 0+1+1
3   count = 0+1+1+1
0   count = 0+1+1+1+1
11  count = 0+1+1+1+1+1
4   count = 0+1+1+1+1+1+1 = 6

1