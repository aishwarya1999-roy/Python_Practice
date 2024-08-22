def solve(str1,output,index, ans):
    if index>=len(str1):
        ans.append(''.join(output[:]))
        return
    


nums = [1,2,3]
ind = 0
ans = []
solve(nums,ind,ans)
print(ans)
