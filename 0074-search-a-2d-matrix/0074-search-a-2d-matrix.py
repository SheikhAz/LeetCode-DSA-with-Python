class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top , bot = 0 , row - 1
        while top <= bot:
            r_v = (top + bot) // 2
            if target > matrix[r_v][-1]:
                top = r_v + 1
            elif target < matrix[r_v][0]:
                bot = r_v - 1
            else:
                break
        if not(top <= bot):
            return False
        r_v = (top + bot) // 2
        l , r = 0 , col - 1
        while r >= l:
            mid = (l + r) //2
            if target > matrix[r_v][mid]:
                l = mid + 1
            elif target < matrix[r_v][mid]:
                r = mid - 1
            else:
                return True
        return False 