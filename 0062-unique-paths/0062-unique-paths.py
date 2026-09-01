class Solution(object):
    def uniquePaths(self, m, n):
        row = [1]*n
        for i in range(m-1):
            Newrow = [1]*n
            for j in range(n-2,-1,-1):
                Newrow[j] = Newrow[j + 1] + row[j]
            row = Newrow
        return row[0]
        