def rev(ss, i, h):
    if i>h:
        return ss
    aa = list(ss)
    aa[i],aa[h] = aa[h],aa[i]
    new_str = "".join(aa)
    print(new_str)
    return rev(new_str, i+1, h-1)

ss = "abaa"
ans = (rev(ss,0,len(ss)-1))
if ans==ss:
    print("Pallindrom")
else:
    print("Not Pallindrom")