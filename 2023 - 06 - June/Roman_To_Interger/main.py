"""class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for key, val in dict_roman.items():
            if s == key:
                print(int(val))

S = Solution()
S.romanToInt('I')"""


dict_roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
minus = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
S = "IV"
L = 0
sliced = [x for x in S]
for key, val in dict_roman.items():
    for i in sliced:
        if key == i:
            if S in minus:
                L = val - L
            elif 

            else:
                L = L+val
print(L)







"""def romanToInt(x: str) :
    dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}
    #d = int(''.join([val if key == x else None for (key, val) in dict_roman.items()]))
    d = [val if x == key else None for (key, val) in dict_roman.items()]
    print(d)


romanToInt('I')"""

