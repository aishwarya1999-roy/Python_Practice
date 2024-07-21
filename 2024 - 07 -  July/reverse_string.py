#Reverse Words

def reverseWords(S):
    a = ".".join(S.split(".")[::-1])
    return a

S = "i.like.this.program.very.much"

print(reverseWords(S))

#Reverse Words - without using the built-in split, join, and reverse functions
"""def reverseWords(S):
    result = ""
    words = []
    curr_word = ""
    for i in range(len(S)):
        if(S[i] == '.'):
            words.append(curr_word)
            curr_word = ""
        else:
            curr_word += S[i]
    words.append(curr_word)
    for i in range(len(words) - 1, -1, -1):
        result += words[i]
        if(i):
            result += "."
    return result

S = "i.like.this.program.very.much"

print(reverseWords(S))"""