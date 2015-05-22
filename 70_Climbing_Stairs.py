# 2015-05-22  Runtime: 56 ms
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        # Let f(n) is the number of distinct ways, f(n) = f(n-1) + f(n-2), f(0) = 1, f(1) = 1, f(2) = 2
        a, b = 1, 1
        for i in xrange(n - 1): a, b = b, a + b
        return b