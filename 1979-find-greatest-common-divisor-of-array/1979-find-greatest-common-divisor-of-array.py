class Solution(object):
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)
        maxi = float('-inf')

        for i in range(2,a+1):
            if a % i == 0 and b % i == 0:
                maxi = max(maxi , i)
        
        return maxi if maxi > 1 else 1


        