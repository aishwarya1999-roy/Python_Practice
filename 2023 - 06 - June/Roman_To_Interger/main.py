"""class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for key, val in dict_roman.items():
            if s == key:
                print(int(val))

S = Solution()
S.romanToInt('I')"""


dict_roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
S = "VI"
sliced = [x for x in S]
for key, val in dict_roman.items():
    for i in sliced:
        if key == i:
            print(val)






"""def romanToInt(x: str) :
    dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}
    #d = int(''.join([val if key == x else None for (key, val) in dict_roman.items()]))
    d = [val if x == key else None for (key, val) in dict_roman.items()]
    print(d)


romanToInt('I')"""

