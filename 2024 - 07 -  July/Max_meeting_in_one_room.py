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