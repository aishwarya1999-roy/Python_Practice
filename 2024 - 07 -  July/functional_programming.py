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

"""def map_p(my_iter):
    return my_iter**2

nums = [3,4,5,6,7]

y = [map_p(num) for num in nums]

z=list(map(map_p, nums))

print(y)
print(z)
"""

num_list=[10,20,30,40,50]
print("Map example")
print(list(map(lambda x:x*2,num_list)))
print("Filter Example")
print(list(filter(lambda x:x>30,num_list)));
print("Chain Example")
print(list(filter(lambda x:x>30,map(lambda x:x*2,num_list))));
