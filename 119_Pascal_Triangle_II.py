# 2015-06-26  Runtime: 48 ms
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        # thanks to https://leetcode.com/discuss/8364/here-is-my-brief-o-k-solution
        A = [0 for i in xrange(rowIndex + 1)]
        A[0] = 1
        for i in xrange(1, rowIndex + 1):
            for j in xrange(i, 0, -1):
                A[j] += A[j - 1]
        return A