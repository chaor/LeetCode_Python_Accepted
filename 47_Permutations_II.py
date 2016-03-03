# 2016-03-03  30 tests, 128 ms
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n] + p for n in set(nums) for p in self.permuteUnique(nums[:nums.index(n)] + nums[nums.index(n) + 1:])] or [[]]
