# Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.
n = int(input("Enter an integer:"))
list1 = list()
print("The divisors of the number are:")
for i in range(1, n + 1):
    if n % i == 0:
        list1.append(i)
print(list1)
