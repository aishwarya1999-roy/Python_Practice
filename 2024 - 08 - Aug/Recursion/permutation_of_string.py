# def solve(str1,output,index, ans):
#     if index>=len(str1):
#         ans.append(''.join(output[:]))
#         return
    


# str1 = "abc"
# output= []
# ans = []
# solve(str1,output, 0, ans)
# print(ans)



str1 = ['a','b','c']
aa = str1
ind = 0
for i in str1:
    if str1.index(i) > 0:
        aa[str1.index(i)],aa[0] = aa[0], aa[str1.index(i)]
    print(''.join(str1))