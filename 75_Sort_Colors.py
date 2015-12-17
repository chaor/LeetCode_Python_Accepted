# 2015-09-12   Runtime: 44 ms
class Solution(object):
    def sortColors(self, A):
        """
        :type A: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # thanks to https://leetcode.com/discuss/17000/share-my-one-pass-constant-space-10-line-solution
        i, p0, p2 = 0, 0, len(A) - 1
        while i <= p2:
            while A[i] == 2 and i < p2:
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1
            while A[i] == 0 and i > p0:
                A[i], A[p0] = A[p0], A[i]
                p0 += 1
            i += 1