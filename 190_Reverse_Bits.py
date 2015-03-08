# 20150307  Runtime: 60 ms

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in xrange(32):
            if n & 1 == 1:
                ret += 1 << (31 - i)
            n >>= 1
        return ret