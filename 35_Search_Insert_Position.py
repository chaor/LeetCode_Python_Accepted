# 2015-05-28  Runtime: 60 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        L, R = 0, len(nums) - 1
        while L < R:
            M = (L + R) / 2
            if target > nums[M]:
                L = M + 1  # index 0, 1, ... M can be excluded
            else:
                R = M  # index M + 1, M + 2, ... len(nums) - 1 can be excluded
        # finally L == R
        return L if target <= nums[L] else L + 1