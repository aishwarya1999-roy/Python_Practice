# File handling

"""fhr=open("data.txt","r")
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
fhr.close()"""


#  tell() method to get current position which is pointed by file object within the file.
# file_object.tell()

#  seek() function to navigate the file object pointer to the required position specified.
"""fhr=open("data.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()"""


# file_object.closed: closed attribute returns true if the file is closed else it will return false.

# file_object.mode: mode attribute returns mode in which the file has been opened.

# file_object.name: name attribute returns the name of the file opened.

