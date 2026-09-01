class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        col = len(obstacleGrid[0])
        row = [0]*col
        row[-1] = 1
        for i in range(len(obstacleGrid)-1,-1,-1):
            newRow = [0]*col
            for j in range(col-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    newRow[j] = 0
                elif col-1 == j:
                    newRow[j]=row[j]
                else:
                    newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
        