class Solution(object):
    def divide(self, dividend, divisor):
        numo = abs(dividend)
        deno = abs(divisor)
        output = 0
        while numo >= deno:
            temp = deno
            mul = 1
            while numo >= temp:
                numo -= temp
                output += mul
                mul += mul
                temp += temp
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            output =  -(output)
        return min(2147483647 , max(-2147483648 , output))
        