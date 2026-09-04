class Solution(object):
    def eventualSafeNodes(self, graph):
        result = []
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for c in graph[i]:
                if not dfs(c):
                    return safe[i]
            safe[i] = True
            return safe[i]
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result