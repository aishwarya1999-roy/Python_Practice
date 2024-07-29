def process_customer_requests(H, supervisor_data, customer_requests):
    on_duty_heights = [-1] * (H + 1)
    for height, start, end in supervisor_data:
        for hour in range(start, end + 1):
            if on_duty_heights[hour] == -1:
                on_duty_heights[hour] = height
            else:
                on_duty_heights[hour] = max(on_duty_heights[hour], height)
    
    results = []
    for customer in customers:
        customer_height, visit_timing = customer
        
        if visit_timing > Hourperday:
            results.append("NO")
            continue
        
        if on_duty_heights[visit_timing] == -1 or customer_height > on_duty_heights[visit_timing]:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Example usage:
string1 = input().split()

H = int(string1[0])
S = int(string1[1])
R = int(string1[2])
string2 = [input() for _ in range(S)]
supervisor_data = [tuple(map(int, s.split())) for s in string2]

string3 = [input() for _ in range(R)]
customer_requests  = [tuple(map(int, s.split())) for s in string3]

results = process_customer_requests(H, supervisor_data, customer_requests)
for result in results:
    print(result)