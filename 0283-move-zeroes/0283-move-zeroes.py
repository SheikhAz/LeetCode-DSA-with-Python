class Solution(object):
    def moveZeroes(self, nums):
        z = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[z],nums[i] = nums[i],nums[z]
                z += 1
        return nums

        