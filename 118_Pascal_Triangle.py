# 2015-06-26  Runtime: 44 ms
class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = [[1]]
        for i in xrange(1, numRows):
            currRow = [1]
            for j in xrange(1, i): currRow.append(res[-1][j - 1] + res[-1][j])
            currRow.append(1)
            res.append(currRow)
        return res