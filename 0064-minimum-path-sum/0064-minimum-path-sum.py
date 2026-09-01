class Solution(object):
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])
        result = [[float("inf")]*(col + 1) for r in range(row+1)]
        result[row - 1][col] = 0
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                result[i][j] = grid[i][j] + min(result[i + 1][j],result[i][j+1])
        return result[0][0]
        