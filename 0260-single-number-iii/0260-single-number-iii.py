class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor = xor ^ n
        diff = 1
        while not (xor & diff):
            diff = diff << 1
        a = 0
        b = 0
        for n in nums:
            if (diff & n):
                a = a ^ n
            else:
                b = b ^ n
        return [a,b]
        