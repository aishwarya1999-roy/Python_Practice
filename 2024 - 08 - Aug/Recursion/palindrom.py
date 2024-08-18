def rev(ss, i, h):
    if i>h:
        return
    aa = list(ss)
    aa[i],aa[h] = aa[h],aa[i]
    new_str = "".join(aa)
    if new_str == ss:
        return True
    return rev(ss, i+1, h-1)

ss = "abaa"
ans = (rev(ss,0,len(ss)-1))
if ans is True:
    print("Pallindrom")
else:
    print("Not Pallindrom")