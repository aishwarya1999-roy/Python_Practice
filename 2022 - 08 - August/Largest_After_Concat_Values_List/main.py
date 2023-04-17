#Write a python function, create_largest_number(), which accepts a list of numbers and returns
# the largest number possible by concatenating the list of numbers.
#Note: Assume that all the numbers are two digit numbers.


def create_largest_number(number_list):
    num=""
    number_list=sorted(number_list)
    for x in range(-1,-len(number_list)-1,-1):
        num+=str(number_list[x])
    return int(num)
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
