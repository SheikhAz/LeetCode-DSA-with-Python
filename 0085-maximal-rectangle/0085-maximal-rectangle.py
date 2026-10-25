class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])

        height = [0] *(col + 1)
        max_area = 0

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
        
            stack = []
            for c in range(col + 1):
                while stack and height[stack[-1]] > height[c]:
                    heights = height[stack.pop()]
                    width = (c if not stack
                            else c - stack[-1] - 1)
                    max_area = max(max_area , heights*width)
                stack.append(c)
        return max_area