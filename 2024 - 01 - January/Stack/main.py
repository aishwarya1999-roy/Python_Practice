size = 6
stack = []
def push() :
    val = int(input("Enter value to add : "))
    if len(stack)>=size:
        print("Stack Overflow!")
    else :
        stack.append(val)

def pop():
    if isempty():
        print("Stack Underflow!")
    else:
        stack.pop()

def isempty():
    return len(stack) <= 0

while True :
    print("-- Oprations of Stack -- ")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")
    choice = int(input("\nPlease enter your choose : "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        print(stack)
    elif choice == 4:
        exit()
    else :
        print("\nInvalid choice!!");



