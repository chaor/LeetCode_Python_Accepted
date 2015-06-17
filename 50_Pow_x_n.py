# 2015-06-16  Runtime: 60 ms
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0: return 1.0 / self.myPow(x, -n)
        if n == 0: return 1.0
        if n == 1: return x
        if n % 2 == 0:
            return self.myPow(x, n / 2) ** 2
        return self.myPow(x, n / 2) ** 2 * x