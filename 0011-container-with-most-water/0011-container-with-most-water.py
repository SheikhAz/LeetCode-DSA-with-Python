class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxarea = 0
        while j >= i:
            H = min(height[i],height[j])
            W = j - i
            area = H * W
            maxarea = max(area , maxarea)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return maxarea
        