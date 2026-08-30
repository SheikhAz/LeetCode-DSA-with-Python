class Solution(object):
    def solveNQueens(self, n):
        col = set()
        postD = set()
        negtD = set()
        board = [["."]*n for r in range(n)]
        result = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in postD or (r - c) in negtD:
                    continue
                col.add(c)
                postD.add(r + c)
                negtD.add(r - c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                postD.remove(r + c)
                negtD.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result
        