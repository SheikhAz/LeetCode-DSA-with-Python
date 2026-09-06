class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(c):
            visited.add(c)
            for ne in range(n):
                if isConnected[c][ne] == 1 and ne not in visited:
                    dfs(ne)
        for c in range(n):
            if c not in visited:
                count += 1
                dfs(c)
        return count
        