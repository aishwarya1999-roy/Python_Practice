# Given a string containing uppercase characters (A-Z),
# compress the string using Run Length encoding.
# Repetition of character has to be replaced by storing the length of that run.
# Write a python function which performs the run length encoding for a given String and
# returns the run length encoded String

def encode(message):
    output=''
    first=message[0]
    i=1
    count=1
    if len(message)==1:
        output += str(count) + first
    else:
        while len(message)>i:
            if first==message[i]:
                count+=1
            else:
                output+=str(count)+first
                count=1
                first=message[i]

            if i==len(message)-1:
                output += str(count) + first
            i+=1
    return output

#Provide different values for message and test your program
encoded_message=encode("AAAABBBCCCA")
print(encoded_message)