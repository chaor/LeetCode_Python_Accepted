# 2015-05-29  Runtime: 68 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        L, R = 0, len(nums) - 1
        while L < R and nums[L] >= nums[R]:
            M = (L + R) / 2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[L]:
                R = M
            else: # nums[L] == nums[M] == nums[R], can't discard either subarrays, e.g. [1, 1, 1, 0, 1], [1, 0, 1, 1, 1]
                L += 1
        return nums[L]