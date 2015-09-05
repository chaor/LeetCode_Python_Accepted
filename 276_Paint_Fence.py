
# 2015-09-05  Runtime: 52 ms
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # when n > 2, f(n) = (f(n - 1) + f(n - 2)) * (k - 1)
        # let s(n) be ways when the last two posts have the same color, 
        # and d(n) be ways when the last two posts have different colors.
        # d(n) = all ways last time * (k - 1) = (s(n - 1) + d(n - 1)) * (k - 1)
        # s(n) = d(n - 1), no s(n - 1) because no more than two adjacent same color
        # so the result is d(n) + s(n), if we let f(n) = s(n) + d(n), then
        # f(n) = (s(n - 1) + d(n - 1)) * (k - 1) + d(n - 1) = f(n - 1) * (k - 1) + d(n - 1)
        # = (f(n - 1) + f(n - 2)) * (k - 1)
        res = [0, k, k * k]
        while len(res) <= n:
            res += (res[-1] + res[-2]) * (k - 1),
        return res[n]