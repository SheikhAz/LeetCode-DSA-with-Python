class Solution(object):
    def uniformArray(self, nums1):
        mini = nums1[0]
        odd = False
        for i in nums1:
            if i < mini:
                mini = i
            if i & 1:
                odd = True
        if mini & 1:
            return True
        return not odd
        