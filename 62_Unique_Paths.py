# 2015-08-31  Runtime: 56 ms
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # C(m-1+n-1)(m-1)
        if m > n: m, n = n, m
        res = 1
        for i in xrange(1, m):
            res = res * (m + n - 1 - i) / i
        return res