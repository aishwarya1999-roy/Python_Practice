def solve(nums,ind,ans):
    if ind>=len(nums):
        ans.append(nums[:])
        return
    for i in range(ind, len(nums)):
        nums[ind],nums[i] = nums[i],nums[ind] 
        solve(nums,ind+1,ans)
        

nums = [1,2,3]
ind = 0
ans = []
solve(nums,ind,ans)
print(ans)
