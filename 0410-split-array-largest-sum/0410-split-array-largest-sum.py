class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)
        result =high
        def canSplit(largest):
            subarray = 0
            currSum = 0
            for i in nums:
                currSum += i
                if currSum > largest:
                    subarray += 1
                    currSum = i
            return subarray + 1 <= k
        while low <= high:
            mid = low + ((high - low)//2)
            if canSplit(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        