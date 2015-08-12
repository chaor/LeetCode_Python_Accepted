# 2015-08-12  Runtime: 44 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target:
                return M
            if nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        return L