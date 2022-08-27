#Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below and returns the encrypted message.
#Words at odd position -> Reverse It
#Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
#Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
#Perform case sensitive string operations wherever necessary.
#Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea

msg = "the sun rises in the east"
final=[]
d = msg.split()
vowels = ['a', 'e', 'i', 'o', 'u']
for word in range(0, len(d)):
    if word % 2 == 0:
        final.append(d[word][::-1])
    else:
        vowel = ""
        cons = ""
        for i in d[word]:
            if i in vowels:
                vowel += i
            else:
                cons += i
        cons+=vowel
        final.append(''.join(cons))
lk = ''
for k in range(len(final)):
    lk += final[k]+ ' '
print(lk)
