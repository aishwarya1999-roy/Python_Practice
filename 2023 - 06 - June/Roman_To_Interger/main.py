"""def romanToInt(x : str) :
        dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}

        for key, val in dict_roman.items():
            if key == x:
                print(val)
            else:


romanToInt('II')
"""

"""user_input = input("Enter a string: ")
sliced_alphabets = [x for x in user_input]
print("Individual alphabets:", sliced_alphabets)
"""

def romanToInt(x: str) :
    dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}
    d = {val for (key,val) in dict.items() if key == x}
    print(d)

romanToInt('I')