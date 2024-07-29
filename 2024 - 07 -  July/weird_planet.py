def process_customer_requests(H, supervisor_data, customer_requests):
    on_duty_heights = [-1] * (H + 1)
    Hi = max(supervisor_data, key=lambda x: x[0])[0]
    B = min(supervisor_data, key=lambda x: x[1])[1]
    E = max(supervisor_data, key=lambda x: x[2])[2]

    results = []
    

    for cust_height, visit_time in customer_requests:
        if visit_time > H:
            results.append("NO")
            continue

        if on_duty_heights[visit_time] == -1 or cust_height > on_duty_heights[visit_time]:
            results.append("YES")
        else:
            results.append("NO")

    return results

# Example usage:
Hourperday = 12
supervisors = [(50, 2, 5), (40, 3, 6), (60, 2, 7)]  # [(supervisor_height, supervisor_shift_start, supervisor_shift_end)]
customers = [(10, 1), (20, 2), (41, 4), (55, 5), (100, 8)]  # [(customer_height, visit_timing)]

results = process_customer_requests(Hourperday, supervisors, customers)

for result in results:
    print(result)