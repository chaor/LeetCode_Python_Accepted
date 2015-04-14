# 2015-03-31  Runtime: 92 ms

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # thanks to https://leetcode.com/discuss/18330/is-it-best-solution-with-o-n-o-1
        maxProfit1stBuy, maxProfit2ndBuy = -10**10, -10**10 # infinitesimal
        maxProfit1stSell, maxProfit2ndSell = 0, 0
        for price in prices:
            # since you must sell the stock before you buy again,
            # we should update these four variables in certain order: 2ndSell, 2ndBuy, 1stSell, 1stBuy
            maxProfit2ndSell = max(maxProfit2ndSell, maxProfit2ndBuy + price)
            maxProfit2ndBuy = max(maxProfit2ndBuy, maxProfit1stSell - price)
            maxProfit1stSell = max(maxProfit1stSell, maxProfit1stBuy + price)
            maxProfit1stBuy = max(maxProfit1stBuy, -price)
        return maxProfit2ndSell