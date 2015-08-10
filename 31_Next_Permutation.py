# 2015-08-09  Runtime: 60 ms
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        # Find the highest index i such that nums[i] < nums[i+1], call nums[i] violated number
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]: break
            i -= 1
        # If no such index exists, the permutation is the last permutation.
        if i == -1:
            nums.reverse()
            return
        # reverse all numbers after violated number
        nums[i + 1:] = nums[len(nums) - 1: i: -1]
        # find the 1st number larger than the violated number
        j = bisect.bisect_right(nums, nums[i], lo = i + 1, hi = len(nums))
        # swap these two numbers
        nums[i], nums[j] = nums[j], nums[i]