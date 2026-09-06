class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parent = [0] *(n + 1)
        c1 = None
        c2 = None
        for i , j in edges:
            if parent[j] == 0:
                parent[j] = i
            else:
                c1 = [parent[j],j]
                c2 = [i,j]
        par = [i for i in range(n+1)]
        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2:
                return False
            par[p2] = p1
            return True
        for n1,n2 in edges:
            if c2 and [n1,n2] == c2:
                continue
            if not union(n1,n2):
                if c1:
                    return c1
                else:
                    return [n1,n2]
        return c2
        