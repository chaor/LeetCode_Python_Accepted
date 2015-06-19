# 2015-06-19  Runtime: 52 ms
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        # thanks to https://leetcode.com/discuss/17000/share-my-one-pass-constant-space-10-line-solution
        zero, second, i = 0, len(nums) - 1, 0
        while i <= second:
            while nums[i] == 2 and i < second:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1