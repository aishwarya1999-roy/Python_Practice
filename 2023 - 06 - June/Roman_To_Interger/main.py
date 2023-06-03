"""def romanToInt(x : str) :
        dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}

        for key, val in dict_roman.items():
            if key == x:
                print(val)
            else:


romanToInt('II')
"""
# Get a string input from the user
user_input = input("Enter a string: ")

# Slice the string into individual alphabets
sliced_alphabets = [x for x in user_input]

# Print the sliced alphabets
print("Individual alphabets:", sliced_alphabets)
