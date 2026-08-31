class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        preV1 = 1
        preV2 = 1
        for i in range(2,n+1):
            result = preV1 + preV2
            preV1 = preV2
            preV2 = result
        return result
        