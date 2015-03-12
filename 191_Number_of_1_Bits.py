# 2015-03-12  Runtime: 286 ms

class Solution:
    # @param n, an integer
    # @return an integer
    def __init__(self):
        self.hamming8bits = {}
        for i in xrange(256):
            number = i
            bits = 0
            for k in xrange(8):
                if 1 & number == 1:
                    bits += 1
                number >>= 1
            self.hamming8bits[i] = bits
            
    def hammingWeight(self, n):
        res = 0
        for i in xrange(4):
            res += self.hamming8bits[n & 255]
            n >>= 8
        return res