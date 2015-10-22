# 2015-10-22  Runtime: 56 ms
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L, R = 0, len(nums) - 1
        if L == R: return 0
        while L < R:
            if R - L == 1:
                return L if nums[L] > nums[R] else R
            M = (L + R) / 2
            if nums[M] > nums[M + 1]:
                R = M
            else:
                L = M