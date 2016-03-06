# 2016-03-06  156 tests, 48 ms
class Solution(object):
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(A)
        for i in xrange(n):
            while 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
                ind = A[i] - 1
                A[i], A[ind] = A[ind], A[i]
        for i, x in enumerate(A):
            if x != i + 1: return i + 1
        return n + 1
