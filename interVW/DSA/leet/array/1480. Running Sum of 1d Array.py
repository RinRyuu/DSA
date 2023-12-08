'''https://leetcode.com/problems/running-sum-of-1d-array/'''



nums = [1,2,3,1,1,3]
for i in range(1,len(nums)):
    nums[i]+=nums[i-1]
    print(nums)
    