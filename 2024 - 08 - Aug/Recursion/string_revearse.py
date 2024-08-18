def rev(ss, i, h):
    if i>h:
        return
    aa = list(ss)
    aa[i],aa[h] = aa[h],aa[i]
    return rev(ss, i, h)

ss = "abcdef"
i = 0
h = len(ss)
print(rev(ss,i,h))