def process_customer_requests(Hourperday, supervisors, customers):
    results = []
    on_duty_heights = [-1] * (Hourperday + 1)
    for supervisor in supervisors:
        supervisor_height, supervisor_shift_start, supervisor_shift_end = supervisor
        for hour in range(supervisor_shift_start, supervisor_shift_end + 1):
            if on_duty_heights[hour] == -1:
                on_duty_heights[hour] = supervisor_height
            else:
                on_duty_heights[hour] = max(on_duty_heights[hour], supervisor_height)

        
    
    return results

Hourperday = 12
supervisors = [(50, 2, 5), (40, 3, 6), (60, 2, 7)]  # [(supervisor_height, supervisor_shif_start, supervisor_shif_end)]
customers = [(10, 1), (20, 2), (41, 4), (55, 5), (100, 8)]  # [(customer_height, visit_timing)]

results = process_customer_requests(Hourperday, supervisors, customers)

for result in results:
        print(result)