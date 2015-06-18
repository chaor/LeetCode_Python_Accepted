# 2015-06-18  Runtime: 91 ms
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        L, R = 0, x
        while L <= R:
            M = (L + R) / 2
            if M ** 2 <= x < (M + 1) ** 2: return M
            if M ** 2 > x:
                R = M - 1
            else:
                L = M + 1