# 2015-05-11  Runtime: 121 ms
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        ret, x = 0, abs(x)
        while x != 0:
            # handle overflow/underflow
            if ret > 214748364: return 0
            ret = ret * 10 + x % 10
            x /= 10
        return ret * sign