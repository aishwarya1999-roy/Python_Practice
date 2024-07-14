def max_meet(arr):
    arr.sort(key=lambda x: x[1])
    count = 1
    end = arr[0][1]
    for i in range(1,len(arr)):
        if arr[i][0] > end:
            count+=1
            end = arr[i][1]
    return count
start_time = [12, 6, 16, 12, 6, 9 , 16, 6, 17, 5]
end_time = [ 17, 13, 16, 18, 17, 10, 18, 12, 18, 11]
meetings = list(zip(start_time, end_time))
print(max_meet(meetings))