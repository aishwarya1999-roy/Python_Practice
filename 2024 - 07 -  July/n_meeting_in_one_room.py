def max_meet(arr):
    arr.sort(key=lambda x: x[1])
    count = 1
    end = arr[0][1]
    for i in range(1,len(arr)):
        if arr[i][0] > end:
            count+=1
            end = arr[i][1]
    return count
start_time = [3, 1, 8, 5, 0, 5]
end_time = [ 4, 2, 9, 7, 6, 9]
# [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
meetings = list(zip(start_time, end_time))
print(max_meet(meetings))

