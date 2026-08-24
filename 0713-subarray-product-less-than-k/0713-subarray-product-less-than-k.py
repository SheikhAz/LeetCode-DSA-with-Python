class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        product = 1
        left = 0
        result = 0
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product = product//nums[left]
                left += 1
            result += (right - left + 1)
        return result
