def rev(ss, i, h):
    if i>h:
        return
    aa = list(ss)
    aa[i],aa[h] = aa[h],aa[i]
    return rev(ss, i+1, h-1)

ss = "abcdef"
i = 0
h = len(ss)
print(rev(ss,i,h))