# 2015-09-29  Runtime: 120 ms
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or not k: return 0
        n = len(prices)
        if k <= n / 2:
            kthBuy, kthSell = [-sys.maxint] * k, [0] * k
            for price in prices:
                for i in xrange(k - 1, 0, -1):
                    kthSell[i] = max(kthSell[i], kthBuy[i] + price)
                    kthBuy[i] = max(kthBuy[i], kthSell[i - 1] - price)
                kthSell[0] = max(kthSell[0], kthBuy[0] + price)
                kthBuy[0] = max(kthBuy[0], -price)
            return kthSell[k - 1]
        else: # we can do the transaction unlimited times
            res = 0
            for i in xrange(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res