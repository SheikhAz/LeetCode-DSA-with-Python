class Solution(object):
    def maxProduct(self, nums):
        result = max(nums)
        curMax = 1
        curMin = 1
        for i in nums:
            maxi = curMax*i
            mini = curMin*i
            curMax = max(maxi,mini,i)
            curMin = min(maxi,mini,i)
            result = max(curMax,result)
        return result