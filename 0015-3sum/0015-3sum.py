class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = set()
        for i in range(n):
            myset = set()
            for j in range(i+1,n):
                k = -(nums[i]+nums[j])
                if k in myset:
                    temp = [nums[i],nums[j],k]
                    temp.sort()
                    result.add(tuple(temp))
                myset.add(nums[j])
        return [list(ans) for ans in result]
        