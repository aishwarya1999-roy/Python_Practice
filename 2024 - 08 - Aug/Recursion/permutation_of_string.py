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
aa = []
ind = 0
for i in range(len(str1)):
    if i > 0:
        str1[i],str1[0] = str[0], str[i]
        print(str1)