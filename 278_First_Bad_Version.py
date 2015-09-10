# 2015-09-09  Runtime: 40 ms
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 2, n
        while L <= R:
            M = (L + R) / 2
            badM = isBadVersion(M)
            if badM and not isBadVersion(M - 1): return M
            if not badM:
                L = M + 1
            else:
                R = M - 1
        return 1