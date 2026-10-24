class Solution:
    def trap(self, height: list[int]) -> int:
        L = len(height)
        maxLeft = [0] * L
        maxLeft[0] = height[0]

        for i in range(1,L):
            maxLeft[i] = max(height[i],maxLeft[i - 1])
        
        maxRight = [0] * L
        maxRight[-1] = height[-1]

        for i in range(L - 2,-1,-1):
            maxRight[i] = max(maxRight[i + 1],height[i])
        
        sum = 0
        for i in range(L):
            H = min(maxRight[i],maxLeft[i]) - height[i]
            sum += H
        return sum