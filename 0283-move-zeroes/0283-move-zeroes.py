class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        for i in range(0,n):
            if nums[i] == 0:
                for j in range(i+1,n):
                    if nums[j]!=0:
                        nums[i],nums[j]=nums[j],nums[i]
                        break
        return nums

        