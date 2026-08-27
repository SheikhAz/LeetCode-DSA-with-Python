class Solution(object):
    def singleNumber(self, nums):
        one = 0
        two = 0
        for n in nums:
            one = (one^n) & (~two)
            two = (two^n) & (~one)
        return one
        