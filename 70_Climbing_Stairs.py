# 2016-03-28  45 tests, 36 ms
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        a, b = 1, 2
        for i in xrange(n - 2): a, b = b, a + b
        return b
