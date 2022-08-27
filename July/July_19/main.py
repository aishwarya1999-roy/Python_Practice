# 1. Print first n Fibonacci numbers
"""num = int(input("Please give me a positive integer number: "))
# Define a fibonacci function to code in recursion
def fibonacci(n):
    if n in (0, 1): #Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci_sequence = []
for i in range(num):
    fibonacci_sequence.append(fibonacci(i))
print(fibonacci_sequence)
"""

# 2. Job levels 3 , 4 or 5. Hike percentage 3 - 15%, 4 - 7%, 5 - 5%.
"""job_levels = [3, 4, 5]
hike_percent = [15, 7, 5]
jl = int(input("What is your Job Level? "))
current_salary = int(input("What is your current salary? "))
if jl in job_levels:
    for i in range(0, len(job_levels)):
        if jl == job_levels[i]:
            new_salary = current_salary * (1+hike_percent[i]/100)
    print(int(new_salary))
else:
    print("Invalid Job Level")"""

# 3. factorial of a given number.

"""def fact(n):
    facto = 1
    for i in range(1, n+1):
        facto = facto*i
    return facto
num = int(input("Enter a num : "))
print(fact(num))"""

# 4. Palindrome or not
# easy way
"""def pallin(num):
    rev, r = 0, 0
    t = num
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=int(num/10)
    if rev == t:
        return True
    else:
        return False
n = int(input("Enter a number : "))
rev = pallin(n)
if rev == True:
    print("Palindrome")
else:
    print("Not Palindrome")
"""
# shorter way
"""
def is_palindrome(num):
    for i in range(0, len(str(num))):
        if str(num)[i] == str(num)[i-1]:
            return True
        else:
            return False
print(is_palindrome(121))
"""

"""x, y = 220, 284
a = []
sum1 = 0
s = (x, y)
a.append(s)
for i in s:
    for j in range(1, i):
        dd = i % j
        if dd == 0:
            sum1 += j
print(sum1)"""

# 5. check_amicable_numbers
"""
def amicable_or(x, y):
    fact1, fact2 = [], []
    for j in range(1, x):
        if x % j == 0:
            fact1.append(j)
    for j in range(1, y):
        if y % j == 0:
            fact2.append(j)
    if sum(fact1) == y and sum(fact2) == x:
        return True
    else:
        return False
a, b = 220, 284
if amicable_or(a, b):
    print("Numbers are amicable number")
else:
    print("Numbers are Not amicable Number")"""

# Write a python function to check whether three given numbers can form the sides of a triangle.
# Hint: Three numbers can be the sides of a triangle if none of the numbers are
# greater than or equal to the sum of the other two numbers.

'''x, y, z = 3, 4, 5
if x >= (y + z) or y >= (x + z) or z >= (x + y):
    print("Triangle can't be formed")
else:
    print("Triangle can be formed")
'''
#another way

"""def form_triangle(num1,num2,num3):
    success = "Triangle can be formed"
    failure = "Triangle can't be formed"
    if num1 >= (num2 + num3) or num2 >= (num1 + num3) or num3 >= (num2 + num1):
        return failure
    else:
        return success
print(form_triangle(3, 10, 5))
"""

"""def find_max(num1, num2):
    max_num = -1
    list1 = []
    if num1 < num2:
        for i in range(num1, num2 + 1):
            if len(str(i)) == 2 and i % 5 == 0 and i%3 == 0:
                list1.append(i)
                max_num = max(list1)
    else:
        return max_num
    return max_num
max_num = find_max(10, 15)
print(max_num)
"""

# Array in python

"""import array as arr
# creating an array with integer type
a = arr.array('i', [4, 6, 5]) # 'i' for int , 'f' for float, 'd' for double

# printing original array
print("The new created array is : ", end=" ")
for i in range(0,len(a)):
    print(a[i])
a.insert(1, 3) #insert to add
print(a)
a.pop(3) #delete value from the location entered
print(a)
print(a[1:])"""

"""# python code to demonstrate working of zip()
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers
for question, answer in zip(questions, answers):
	print('What is your {0}? I am {1}.'.format(question, answer))"""

"""dict1 = {"name": "apple", 'color': 'red', 'shape': 'circle'}
for key, value in dict1.items():
    print('What is your', key, '?  I am', value)"""

# sort,reverse & set - set remove duplicate
"""lis = [1, 3, 5, 3, 9, 5, 6, 2, 1, 3]
L = sorted(lis)
print(L)
print(sorted(set(lis)))
print("The list in reversed order is : ")
for i in reversed(L):
    print(i, end=" ")"""


