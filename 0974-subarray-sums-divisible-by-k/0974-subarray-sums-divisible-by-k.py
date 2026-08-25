class Solution(object):
    def subarraysDivByK(self, nums, k):
        sums = 0
        prefixSum = {0:1}
        result = 0
        for n in nums:
            sums += n
            remain = sums % k
            result += prefixSum.get(remain,0)
            prefixSum[remain] = 1 + prefixSum.get(remain,0)
        return result