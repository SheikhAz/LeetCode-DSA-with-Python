class Solution(object):
    def subarraySum(self, nums, k):
        result = 0
        sums = 0
        prefixSum = {0:1}
        for n in nums:
            sums += n
            diff = sums - k
            result += prefixSum.get(diff,0)
            prefixSum[sums] = 1 + prefixSum.get(sums,0)
        return result

        