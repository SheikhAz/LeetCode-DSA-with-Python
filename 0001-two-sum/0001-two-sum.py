class Solution(object):
    def twoSum(self, nums, target):
        result = {}
        for i in range(len(nums)):
            sum = target - nums[i]
            if sum in result:
                return [result[sum],i]
            result[nums[i]] = i
        
                
        