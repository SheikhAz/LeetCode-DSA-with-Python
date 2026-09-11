class Solution(object):
    def nextGreaterElements(self, nums):
        result = [-1]*len(nums)
        stack = []
        n = len(nums)

        for i in range(2*n - 1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i%n]:
                stack.pop()
            if i < n:
                if stack:
                    result[i] = nums[stack[-1]]
            stack.append(i%n)
        
        return result
        