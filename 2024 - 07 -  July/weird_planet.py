def process_customer_requests(H, supervisor_data, customer_requests):
    on_duty_heights = [-1] * (H + 1)
    for height, start, end in supervisor_data:
       max_height = max(height)
    
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