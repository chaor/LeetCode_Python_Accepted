# 2016-02-21  Runtime: 60 ms
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # from right to left find longest increasing sequence
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]: i -= 1
        # swap nums[i - 1] and min(number in nums[i...end] which is larger than nums[i - 1])
        # consider it as a carry to nums[i - 1]
        if i > 0:
            j, pre = len(nums) - 1, nums[i - 1]
            while j >= i and nums[j] <= pre: j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        # reverse nums[i...end]
        k = len(nums) - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i, k = i + 1, k - 1
