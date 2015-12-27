# 2015-12-27  180 tests, 1544ms
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [0] + [amount + 1] * amount
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a], dp[a - c] + 1)
        return -1 if dp[-1] > amount else dp[-1]
