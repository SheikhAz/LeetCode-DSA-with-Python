class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        l , r = 0 , x
        while l <= r:
            m = l + ((r - l)//2)
            if m*m > x:
                r = m - 1
            elif m*m < x:
                l = m + 1
                result = m
            else:
                return m
        return result 