def rev(ss, i, h):
    if i>h:
        return ss
    aa = list(ss)
    aa[i],aa[h] = aa[h],aa[i]
    new_str = "".join(aa)
    if new_str == ss:
        return True
    return rev("".join(aa), i+1, h-1)

ss = "abcdef"
print(rev(ss,0,len(ss)-1))