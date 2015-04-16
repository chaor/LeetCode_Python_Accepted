# 2015-04-15  Runtime: 180 ms

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        # find the leftmost common digits of all 1's for m and n. 
        # if m=1110001, n=1110111, just need to find 1110000 and it will be the answer.
        mask = 2**31 - 1
        while mask & n != mask & m: mask <<= 1
        return mask & m