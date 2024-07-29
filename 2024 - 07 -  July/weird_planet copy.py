def process_customer_requests(Hourperday, supervisors, customers):
    results = []
    for customer in customers:
        customer_height, visit_timing = customer
        
        if visit_timing > Hourperday:
            results.append("No")
            continue
        
        not_accepted = False
        for supervisor in supervisors:
            supervisor_height, supervisor_shif_start, supervisor_shif_end = supervisor
            if customer_height > supervisor_height or visit_timing < supervisor_shif_start or visit_timing > supervisor_shif_end:
                continue
            else:
                not_accepted = True
                break
        
        if not_accepted:
            results.append("No")
        else:
            results.append("Yes")
    
    return results

Hourperday = 12
supervisors = [(50, 2, 5), (40, 3, 6), (60, 2, 7)]  # [(supervisor_height, supervisor_shif_start, supervisor_shif_end)]
customers = [(10, 1), (20, 2), (41, 4), (55, 5), (100, 8)]  # [(customer_height, visit_timing)]

results = process_customer_requests(Hourperday, supervisors, customers)

for result in results:
        print(result)