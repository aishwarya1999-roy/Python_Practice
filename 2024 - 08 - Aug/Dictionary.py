a = {
    "Name" : 2,
    "Age" : 4,
    "call" : 6
}
b = {
    4 : 5,
    5 : 7,
    6 : 8
}
print("a :", a)

b = a.copy()
print("b :", b)
b["sc"] = 8
print("b :", b)
print("a :", a)
