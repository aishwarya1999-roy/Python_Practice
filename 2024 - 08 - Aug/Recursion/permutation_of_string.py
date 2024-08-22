# def solve(str1,output,index, ans):
#     if index>=len(str1):
#         ans.append(''.join(output[:]))
#         return
    


# str1 = "abc"
# output= []
# ans = []
# solve(str1,output, 0, ans)
# print(ans)



ast  = "abc"
out =[]
ans = []
for i in range(0,5):
    for j in range(i+1,len(ast)):
        ans.append(ast[i]+ast[j])

print(ans)