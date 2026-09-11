class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        num1Ind = {n:i for i,n in enumerate(nums1)}
        result = [-1]*len(nums1)

        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                idx = num1Ind[val]
                result[idx] = cur
            if cur in num1Ind:
                stack.append(cur)
            
        return result