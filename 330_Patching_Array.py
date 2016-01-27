# 2015-01-26  149 tests, 48 ms
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i, patchCount, maxReach, numLength = 0, 0, 1, len(nums)
        while maxReach <= n:
            if i < numLength and nums[i] <= maxReach:
                maxReach += nums[i]
                i += 1
            else:
                maxReach <<= 1
                patchCount += 1 # add maxReach into nums
        return patchCount
