def rev(ss, i, h):
    aa = list(ss)
    if i>h:
        return "".join(aa)
    aa[i],aa[h] = aa[h],aa[i]
    return rev(aa, i+1, h-1)

ss = "abcdef"
i = 0
h = len(ss)-1
print(rev(ss,i,h))