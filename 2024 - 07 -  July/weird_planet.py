def process_customer_requests(H, supervisor_data, customer_requests):
    on_duty_heights = [-1] * (H + 1)
    for height, start, end in supervisor_data:
        for hour in range(start, end + 1):
            if on_duty_heights[hour] == -1:
                on_duty_heights[hour] = height
            else:
                on_duty_heights[hour] = max(on_duty_heights[hour], height)
    
    results = []
    for cust_height, visit_time in customer_requests:
        if on_duty_heights[visit_time] == -1 or cust_height > on_duty_heights[visit_time]:
            results.append("YES")
        else:
            results.append("NO")

    return results

# Example usage:
H = 10
supervisor_data = [(50, 2, 5), (40, 3, 6), (60, 2, 7)]
customer_requests = [(10, 1), (10, 2), (50, 5), (51, 6), (100, 10)]

results = process_customer_requests(H, supervisor_data, customer_requests)
for result in results:
    print(result)