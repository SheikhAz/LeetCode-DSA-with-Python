class Solution(object):
    def findRotation(self, mat, target):
        for _ in range(4):
            if mat == target:
                return True
            self.rotate(mat)
        return False

    def rotate(self,mat):
        n = len(mat)
        for i in range(0,n - 1):
            for j in range(i+1 , n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        for i in range(n):
            mat[i].reverse()

        