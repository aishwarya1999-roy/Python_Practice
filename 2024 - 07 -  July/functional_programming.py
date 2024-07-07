"""def add(x,y):
    return x+y
print(add(5,6))"""

#Lambda function

"""add2= lambda x,y : x+y
print(add2(5,4))


print((lambda x,y : x+y)(6,4))"""

# mannual map function

"""def map_p(my_func, my_iter):
    res =[]
    for i in my_iter:
        new_item = my_func(i)
        res.append(new_item)
    return(res)
nums = [3,4,5,6,7]

squared = map_p(lambda x: x**2, nums)
print(squared)
"""
#map function
"""def map_p(my_iter):
    return my_iter**2

nums = [3,4,5,6,7]

y = [map_p(num) for num in nums] #list comprehension

z=list(map(map_p, nums))#map function

print(y)
print(z)
"""

# filter function

"""nums = [5,9,14,21,566]

def even(x):
    return x&1

print(list(filter(even,nums)))"""

#reduce function    
"""from functools import reduce
arr1 = [1,1,5,4,3,3,5,6,7,2,7,6,2]"""


from functools import reduce

"""arr1 = [3,2,1,4,5] 
print(reduce(lambda x,y : x+y, arr1)) #print sum
print(reduce(lambda x,y : x if x>y else y, arr1)) #print max
print(reduce(lambda x,y : x if x<y else y, arr1)) #print min

print(list(filter(lambda x: x&1, arr1))) #print odd 
print(list(map(lambda x: "Odd" if x&1 == 1 else "even", arr1))) #print odd or even"""


#find the unique element (which is only one occurance in list) from a list of numbers
arr1 = [1,1,5,4,3,3,5,6,7,2,7,6,2]
print(reduce(lambda x,y : x^y, arr1))
print(reduce(lambda x,y : x if x>y else y, arr1))


print(1 ^ 1 ^ 5 ^ 3 ^ 3 ^ 5 ^ 6 ^ 7 ^ 2 ^ 7 ^ 6 ^ 2 ^ 4)

