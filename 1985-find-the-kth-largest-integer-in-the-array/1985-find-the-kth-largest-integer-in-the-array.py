class Solution(object):
    def kthLargestNumber(self, nums, k):
        nums = list(map(int,nums))
        nums.sort()
        return str(nums[len(nums)-k])
        