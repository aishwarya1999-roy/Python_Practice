# Print first n Fibonacci numbers

num = int(input("Please give me a positive integer number: "))
# Define a fibonacci function to code in recursion
def fibonacci(n):
    if n in (0, 1): #Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci_sequence = []
for i in range(num):
    fibonacci_sequence.append(fibonacci(i))
print(fibonacci_sequence)