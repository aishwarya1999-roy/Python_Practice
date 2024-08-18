# def rev(ss, i, h):
#     if i>h:
#         return ss
#     aa = list(ss)
#     aa[i],aa[h] = aa[h],aa[i]
#     return rev("".join(aa), i+1, h-1)

# ss = "abbaa"
# ans = (rev(ss,0,len(ss)-1))
# if ans==ss:
#     print("Pallindrom")
# else:
#     print("Not Pallindrom")

# def rev(ss, i, h):
#     if i>h:
#         return True
#     if str[i]!=str[h]:
#         return False
#     else:
#         return rev(ss, i+1, h-1)

# ss = "abbaa"
# ans = rev(ss,0,len(ss)-1)
# if ans is True:
#     print("Pallindrom")
# else:
#     print("Not Pallindrom")
