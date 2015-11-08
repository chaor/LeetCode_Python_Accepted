# 2015-11-08  Runtime: 36 ms
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob(L, R):
            include, exclude = 0, 0
            for k in range(L, R + 1):
                i, e = include, exclude
                include, exclude = nums[k] + e, max(i, e)
            return max(include, exclude)

        if len(nums) == 1: return nums[0]
        return max(rob(0, len(nums) - 2), rob(1, len(nums) - 1))