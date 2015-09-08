# 2015-09-07  Runtime: 60 ms
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        # thanks to https://leetcode.com/discuss/9459/o-logn-solution-in-java
        if n < 0:
            x, n = 1.0 / x, -n
        res, f = 1, x
        while n > 0:
            if n % 2: res *= f
            f = f * f
            n >>= 1
        return res