# 2015-07-06  Runtime: 60 ms
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0: return False
        return not n & (n - 1)