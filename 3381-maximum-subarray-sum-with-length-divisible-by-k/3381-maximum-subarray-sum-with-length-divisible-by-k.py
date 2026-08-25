class Solution(object):
    def maxSubarraySum(self, nums, k):
        sums = 0
        prefixSum = {0:0}
        result = float('-inf')
        for i ,n in enumerate(nums):
            sums += n
            length = i + 1
            remain = length % k
            if remain in prefixSum:
                result = max(result, sums - prefixSum[remain])
                prefixSum[remain]=min(sums,prefixSum[remain])
            else:
                prefixSum[remain] = sums
        return result
        