# 2015-08-12  Runtime: 52 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        # thanks to https://leetcode.com/discuss/18242/clean-iterative-solution-binary-searches-with-explanation
        L, R, result = 0, len(nums) - 1, [-1, -1]
        # search for the left one
        while L < R:
            M = (L + R) / 2 # biased to left
            if nums[M] < target:
                L = M + 1
            else:
                R = M
        if nums[L] != target:
            return result
        result[0] = L
        R = len(nums) - 1
        while L < R:
            M = (L + R) / 2 + 1 # biased to right
            if nums[M] > target:
                R = M - 1
            else:
                L = M
        result[1] = R
        return result