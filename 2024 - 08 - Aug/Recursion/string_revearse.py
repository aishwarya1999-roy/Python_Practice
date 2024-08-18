def rev(ss, i, h):
    print("i: " , i, "h :",h)
    aa = list(ss)
    if i>h:
        return aa
    aa[i],aa[h] = aa[h],aa[i]
    return rev(ss, i+1, h-1)

ss = "abcdef"
i = 0
h = len(ss)-1
print(rev(ss,i,h))