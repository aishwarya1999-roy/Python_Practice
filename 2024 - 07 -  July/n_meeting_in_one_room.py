"""def max_meet(arr):
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
meetings = list(zip(start_time, end_time))
print(max_meet(meetings))"""





###################

def maxMeetings(start_time, end_time):
    meetings = [(start_time[i], end_time[i], i+1) for i in range(len(start_time))]
    meetings.sort(key=lambda x: x[1])
    selected_meetings = []
    last_finish_time = -1
    
    for start, finish, index in meetings:
        if start > last_finish_time:
            selected_meetings.append(index)
            last_finish_time = finish
            
    return sorted(selected_meetings)

S = [12, 6, 16, 12, 6, 9 , 16, 6, 17, 5]
F =  [ 17, 13, 16, 18, 17, 10, 18, 12, 18, 11]

selected_meetings = maxMeetings(S, F)
print("The meetings that can be accommodated are:", selected_meetings)
