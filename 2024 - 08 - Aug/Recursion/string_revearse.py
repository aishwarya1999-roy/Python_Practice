def rev(ss):
    dd = "".join(list(ss)[::-1])
    return type(dd)

ss = "abcdef"
print(rev(ss))