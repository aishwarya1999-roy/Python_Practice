def romanToInt(x : str) :
        dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}

        for key, val in dict_roman.items():
            if key == x:
                print(val)
           

romanToInt('II')
