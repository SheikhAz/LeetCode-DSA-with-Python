class Solution(object):
    def maxAreaOfIsland(self, grid):
        area = 0
        row = len(grid)
        col = len(grid[0])
        visit = set()
        def dfs(r,c):
            if (r < 0 or c < 0 or r ==row or c == col or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1 + dfs(r + 1,c) + dfs(r -1,c) + dfs(r,c+1) + dfs(r,c-1)) 
        for r in range(row):
            for c in range(col):
                area = max(area,dfs(r,c))
        return area
        