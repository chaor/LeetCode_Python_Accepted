# 2015-03-30  Runtime: 97 ms

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        # find the max diff, the larger number must come after the smaller number
        if not prices:
            return 0
        minPrice, diff = 10**10, -10**10
        for price in prices:
            minPrice = min(minPrice, price)
            diff = max(diff, price - minPrice)
        return diff