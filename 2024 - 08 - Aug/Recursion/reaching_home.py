#reaching home - level 0 recursion
def reach_home(dest, sour):
    print("Source : ", sour, "Destination : ", dest)
    if sour == dest:
        return "Reached Home"
    
    return reach_home(dest, sour+1)

dest = int(input("Destination : "))
sour = int(input("Source : "))
print(reach_home(dest, sour))