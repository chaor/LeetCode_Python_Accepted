# 2015-06-10  Runtime: 60 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target: return M
            if nums[L] <= nums[M]:
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
        return -1