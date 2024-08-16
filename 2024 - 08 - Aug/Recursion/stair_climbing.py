#stair climbing
def stair(dest):
    print("position : ", dest)
    #base case
    if dest<0:
        return 0
    if dest == 0:
        return 1
    return stair(dest-1) + stair(dest-2)
dest = int(input("Destination : "))
print(stair(dest))