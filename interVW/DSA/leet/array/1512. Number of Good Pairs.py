class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    count = count+1
        return count