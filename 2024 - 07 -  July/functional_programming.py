"""def add(x,y):
    return x+y
print(add(5,6))"""


"""add2= lambda x,y : x+y
print(add2(5,4))


print((lambda x,y : x+y)(6,4))"""

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
"""nums = [3,4,5,6,7]

squared = list(map(lambda x: x**2, nums))
print(squared)
"""
nums = [3,4,5,6,7]
db = lambda x: x**2
print(db(nums))