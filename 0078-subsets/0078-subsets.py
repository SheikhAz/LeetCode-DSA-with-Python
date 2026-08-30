class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        total_set = 1<<n
        result = []
        for s in range(0,total_set):
            lst = []
            for i in range(0,n):
                if s & (1<<i) != 0:
                    lst.append(nums[i])
            result.append(lst)
        return result
        