# 2015-02-05  Runtime: 86 ms

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in A:
            res ^= i
        return res