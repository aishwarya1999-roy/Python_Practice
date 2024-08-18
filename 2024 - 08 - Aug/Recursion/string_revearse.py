def rev(ss, i, h):
    if i>h:
        return "".join(aa)
    ss[i],ss[h] = ss[h],ss[i]
    return rev(ss, i+1, h-1)

ss = "abcdef"
print(rev(ss,0,len(ss)-1))
