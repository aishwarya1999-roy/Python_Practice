def solve(str1,output,index, ans):
    if index>=len(str1):
        ans.append(''.join(output[:]))
        return
    


str1 = [1,2,3]
output= []
ans = []
solve(str1,output, 0, ans)
print(ans)
