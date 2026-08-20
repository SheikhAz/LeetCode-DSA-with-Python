class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        result = high
        def canShip(cap):
            ship = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = cap
                currCap -= w
            return ship <= days
        while low <= high:
            cap = (low+high)//2
            if canShip(cap):
                result = min(result,cap)
                high = cap - 1
            else:
                low = cap + 1
        return result
        