# 2015-08-15  Runtime: 132 ms

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, A):
        if len(A) == 1: return [A]
        A.sort()
        res, prev = [], None
        for i in xrange(len(A)):
            if A[i] == prev: continue
            prev = A[i]
            for x in self.permuteUnique(A[:i] + A[i + 1:]):
                res.append([A[i]] + x)
        return res