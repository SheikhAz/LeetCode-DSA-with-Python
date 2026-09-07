class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n
    def find(self, x):
        while x!= self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x1,x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True            

class Solution(object):
    def accountsMerge(self, accounts):
        uf = UnionFind(len(accounts))
        emailtoAcc = {}

        for i ,a in enumerate(accounts):
            for e in a[1:]:
                if e in  emailtoAcc:
                    uf.union(i,emailtoAcc[e])
                else:
                    emailtoAcc[e] = i
        
        emailGroup = defaultdict(list)
        for e , i in emailtoAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        result = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            result.append([name] + sorted(emailGroup[i]))

        return result
        