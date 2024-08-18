def rev(ss, i, h):
    
    aa = list(ss)
    if i>h:
        return
    aa[i],aa[h] = aa[h],aa[i]
    print(aa)
    return rev(ss, i+1, h-1)

ss = "abcdef"
i = 0
h = len(ss)-1
print(rev(ss,i,h))