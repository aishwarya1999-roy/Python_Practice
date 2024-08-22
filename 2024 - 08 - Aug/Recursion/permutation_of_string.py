def solve(nums,ind,ans):
    if ind>=len(nums):
        ans.append(nums[:])
        return
    for i in range(ind, len(nums)):
        nums[ind],nums[i] = nums[i],nums[ind] 
        solve(nums,ind+1,ans)
        nums[ind],nums[i] = nums[i],nums[ind] 

nums = [1,2,3]
ind = 0
ans = []
solve(nums,ind,ans)
print(ans)

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        nums[i],nums[j] = nums[j],nums[i]