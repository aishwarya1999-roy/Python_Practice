# def solve(str1,output,index, ans):
#     if index>=len(str1):
#         ans.append(''.join(output[:]))
#         return
    


# str1 = "abc"
# output= []
# ans = []
# solve(str1,output, 0, ans)
# print(ans)



ast  = ['1','2','3']
out =[]
ans = []
for i in range(1):
    for j in range(1,3):
        ans.append(ast[i]+ast[j])
print(ans)