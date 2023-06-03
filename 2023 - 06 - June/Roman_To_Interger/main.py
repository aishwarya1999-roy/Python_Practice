"""class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for key, val in dict_roman.items():
            if s == key:
                print(int(val))

S = Solution()
S.romanToInt('I')"""


dict_roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
S = "XVI"
L = 0
for i in range(len(S)-1):
    if dict_roman[S[i]] < dict_roman[S[i+1]]:
        L = dict_roman[S[i+1]]- dict_roman[S[i]]

print(L)







"""def romanToInt(x: str) :
    dict_roman = {"I" : "1", "V" : "5", "X" : "10", "L" : "50", "C" : "100", "D" : "500", "M" : "1000"}
    #d = int(''.join([val if key == x else None for (key, val) in dict_roman.items()]))
    d = [val if x == key else None for (key, val) in dict_roman.items()]
    print(d)


romanToInt('I')"""

