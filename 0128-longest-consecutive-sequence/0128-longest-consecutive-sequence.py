class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        longest = 1

        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1
            longest = max(count , longest)
        return longest