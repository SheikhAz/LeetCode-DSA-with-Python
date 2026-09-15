class Solution(object):
    def reverse(self, x):
        MAX = 2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x:
            digit = x % 10
            x = x // 10

            if result > MAX // 10 or (result == MAX//10 and digit >= MAX % 10):
                return 0
            result = result * 10 + digit
        return result * sign
        