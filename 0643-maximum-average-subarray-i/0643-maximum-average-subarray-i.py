class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        sum = 0
        for i in range(0,k):
            sum += nums[i]

        maxSum = sum
        for i in range(k,n):
            sum -= nums[i-k]
            sum += nums[i]
            maxSum = max(maxSum,sum)

        return float(maxSum)/k
        