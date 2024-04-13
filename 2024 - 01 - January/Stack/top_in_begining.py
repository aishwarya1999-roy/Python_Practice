"""stack = []
#val = int(input("Enter value to add : "))
def push(val) :
    stack.insert(0, val)
push(4)
push(6)
print(stack)
#print(stack)"""

stack = []
val = int(input("Enter value to add: "))

def push():
    first = -1
    first = first + 1
    for i in range(first, 0, -1):
        stack[i] = stack[i-1]
    stack[0] = val

push()
print(stack)





