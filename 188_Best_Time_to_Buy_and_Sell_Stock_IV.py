# 2015-04-04  Runtime: 175 ms

class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        if k <= len(prices) / 2:
            # dp[N] means the max profit after Nth buy or sell, N=1,3,5,7... buy, N=0,2,4,6,8... sell
            # 状态转移方程 dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
            dp = [None for i in xrange(2 * k + 1)]
            dp[0] = 0
            for i in xrange(len(prices)):
                for j in xrange(1, min(2 * k + 1, i + 2)):
                    dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
            return max(dp)
        else: # k > len(prices) / 2, we can do unlimited transactions, it becomes Best Time to Buy and Sell Stock II
            sum = 0
            for i in xrange(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    sum += prices[i] - prices[i - 1]
            return sum