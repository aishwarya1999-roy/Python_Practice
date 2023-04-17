# Write a python function to check whether three given numbers can form the sides of a triangle.
# Hint: Three numbers can be the sides of a triangle if none of the numbers are
# greater than or equal to the sum of the other two numbers.

"""x, y, z = 3, 4, 5
if x >= (y + z) or y >= (x + z) or z >= (x + y):
    print("Triangle can't be formed")
else:
    print("Triangle can be formed")
"""
# Another way

def form_triangle(num1,num2,num3):
    success = "Triangle can be formed"
    failure = "Triangle can't be formed"
    if num1 >= (num2 + num3) or num2 >= (num1 + num3) or num3 >= (num2 + num1):
        return failure
    else:
        return success
print(form_triangle(3, 10, 5))
