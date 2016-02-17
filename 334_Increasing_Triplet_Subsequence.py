# 2016-02-17  61 tests, 56 ms
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = [float('inf')] * 3
        for x in nums:
            L[bisect.bisect_left(L, x)] = x
            if L[2] < float('inf'): return True
        return False
