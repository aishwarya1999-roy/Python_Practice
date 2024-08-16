# by accumluator 
def sum_of_array(arr, n, ans):
    
    if n <=0:
        return ans
    ans = ans + arr[0]
    return sum_of_array(arr[1:], n-1,ans)

arr = [5,6,2,1,3]
n = len(arr)
ans = 0
print(sum_of_array(arr, n,ans))

# by direct recursion
# def sum_of_array(arr, n):
#     if n ==0:
#         return 0
#     if n == 1:
#         return arr[0]
#     remain = sum_of_array(arr[1:], n-1)
#     ans = arr[0] + remain
#     return ans

# arr = [5,6,2,1]
# n = len(arr)
# print(sum_of_array(arr, n))

