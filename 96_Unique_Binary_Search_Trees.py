# 2015-03-24  Runtime: 57 ms

class Solution:
    # @return an integer
    def numTrees(self, n):
        # use c[] to represent numTrees
        c = [0 for i in xrange(n + 1)]
        c[0] = 1 # no node
        c[1] = 1 # only one node
        for totalNodes in xrange(2, n + 1):
            for LChildNodes in xrange(totalNodes):
                c[totalNodes] += c[LChildNodes] * c[totalNodes - 1 - LChildNodes] # c[left] * c[right]
        return c[n]