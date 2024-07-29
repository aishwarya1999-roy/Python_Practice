"""import heapq
def huff(arr, f,n):
    dic = dict(zip(arr, list(f)))

    heapq.heapify(arr)
    
    while n>1:
        
        left = heapq.heappop(arr)
        right = heapq.heappop(arr)
        newnode = left + right
        heapq.heappush(arr, newnode)
        print("After : " , arr)
        n=n-1
    rr = newnode
    return rr
 
f = "abcdef"
arr = [5,9,12,13,16,45]
n = len(arr)
print(huff(arr,f, n))"""

