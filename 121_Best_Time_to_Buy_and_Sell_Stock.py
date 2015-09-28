# 2015-09-28  Runtime: 60 ms
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice, res = sys.maxint, 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            if p - minPrice > res:
                res = p - minPrice
        return res