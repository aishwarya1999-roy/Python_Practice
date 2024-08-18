def rev(ss, i, h):
    if i>h:
        return True
    if ss[i]!=ss[h]:
        return False
    else:
        return rev(ss, i+1, h-1)

ss = "abba"
ans = rev(ss,0,len(ss)-1)
if ans is True:
    print("Pallindrom")
else:
    print("Not Pallindrom")
