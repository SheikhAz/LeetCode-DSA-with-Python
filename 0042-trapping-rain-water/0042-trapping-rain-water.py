class Solution(object):
    def trap(self, height):
        L = len(height)
        maxleft = [0]*L
        maxleft[0] = height[0]
        for i in range (1,L):
            maxleft[i] = max(maxleft[i-1],height[i])
        
        maxright = [0]*L
        maxright[-1] = height[-1]
        for i in range (L-2,-1,-1):
            maxright[i] = max(maxright[i+1],height[i])
        
        sum = 0
        for i in range(0,L):
            H = min(maxleft[i],maxright[i]) - height[i]
            sum += H

        return sum

        