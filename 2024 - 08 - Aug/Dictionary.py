a = {
    "id" : 6,
    "Name" : 2,
    "Age" : 4
}
b = {
    4 : 5,
    5 : 7,
    6 : 8
}
# print("a :", a)
# b = a.copy()
# print("b :", b)
# b["call"] = 8
# print("b :", b)
# print("a :", a)
# print(a.keys())
# print(a.values())
# print(a.setdefault("call"))
# print("a :", a)

my_dict = {}
my_dict.setdefault('fruits', []).append('apple')
print(my_dict)  # Output: {'fruits': ['apple']}
