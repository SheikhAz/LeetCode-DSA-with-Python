class Solution(object):
    def dfs(self,r,c,grid,visited):
        if r < 0 or c < 0 or r >= len(grid) or c>= len(grid[0]):
            return
        if grid[r][c] == "0":
            return 
        if visited[r][c] ==1:
            return
        visited[r][c] = 1
        self.dfs(r+1,c,grid,visited)
        self.dfs(r-1,c,grid,visited)
        self.dfs(r,c-1,grid,visited)
        self.dfs(r,c+1,grid,visited)
        
    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] =="1" and visited[r][c] == 0:
                    count += 1
                    self.dfs(r,c,grid,visited)
        return count
        