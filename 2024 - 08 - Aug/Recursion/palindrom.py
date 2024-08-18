def rev(ss, i, h):
    if i>h:
        return ss
    aa = list(ss)
    aa[i],aa[h] = aa[h],aa[i]
    return rev("".join(aa), i+1, h-1)

ss = "abbaa"
ans = (rev(ss,0,len(ss)-1))
if ans==ss:
    print("Pallindrom")
else:
    print("Not Pallindrom")