class Solution(object):
    def permuteUnique(self, nums):
        result = []
        perm = []
        count = {n:0 for n in nums}
        for i in nums:
            count[i] += 1
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm[:])
                return
        
            for i in count:
                if count[i] > 0:
                    perm.append(i)
                    count[i] -= 1
                    dfs()
                    count[i] += 1
                    perm.pop()
        dfs()
        return result