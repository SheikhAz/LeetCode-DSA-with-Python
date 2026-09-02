class Solution(object):
    def change(self, amount, coins):
        dp = [0]*(amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c,amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]