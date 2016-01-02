# 2016-01-01  39 tests, 104 ms
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = (len(nums) + 1) / 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
