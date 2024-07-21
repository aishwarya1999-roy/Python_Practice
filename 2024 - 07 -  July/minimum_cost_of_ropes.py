import heapq
def minCost(arr,n) :
    # Create a min-heap from the list of ropes
    heapq.heapify(ropes)
    
    total_cost = 0
    
    # While there is more than one rope
    while len(ropes) > 1:
        # Extract the two smallest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        # Calculate the cost of connecting them
        cost = first + second
        total_cost += cost
        
        # Insert the new rope back into the heap
        heapq.heappush(ropes, cost)

    return first

arr = [4, 3, 2, 6] # 2, 3, 4, 6
N = 4
print(minCost(arr,N))