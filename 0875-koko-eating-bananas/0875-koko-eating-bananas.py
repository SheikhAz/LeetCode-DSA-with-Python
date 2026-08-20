class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        result = high
        while low <= high:
            k = (low + high)//2
            hour = 0
            for p in piles:
                hour += (p+k-1)//k
            if hour <= h:
                result = min(result,k)
                high = k - 1
            else:
                low = k + 1
        return result
        