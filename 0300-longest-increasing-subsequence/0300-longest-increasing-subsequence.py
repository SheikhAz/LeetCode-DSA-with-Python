import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        result = []
        for n in nums:
            i = bisect.bisect_left(result,n)
            if len(result) == i:
                result.append(n)
            else:
                result[i] = n
        return len(result)
        