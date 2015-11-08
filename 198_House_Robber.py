# 2015-11-08  Runtime: 44 ms
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        include, exclude = 0, 0
        for money in nums:
            include, exclude = money + exclude, max(include, exclude)
        return max(include, exclude)