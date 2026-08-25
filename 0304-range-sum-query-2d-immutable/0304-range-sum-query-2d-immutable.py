class NumMatrix(object):

    def __init__(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        self.NumMatrix = [[0]*(col + 1) for r in range(row + 1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                above = self.NumMatrix[r][c + 1]
                self.NumMatrix[r + 1][c + 1] = prefix + above        
    def sumRegion(self, row1, col1, row2, col2):
        row1 = row1 + 1
        row2 = row2 + 1
        col1 = col1 + 1
        col2 = col2 + 1

        bottonRight = self.NumMatrix[row2][col2]
        above = self.NumMatrix[row1 - 1][col2]
        left = self.NumMatrix[row2][col1 - 1]
        topLeft = self.NumMatrix[row1 - 1][col1 - 1]
        return bottonRight - above - left + topLeft
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)