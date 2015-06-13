# 2015-06-12  Runtime: 64 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) / 2
            if nums[M] == target: return True
            if nums[L] < nums[M]: # M's left is ascending
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            elif nums[L] > nums[M]: # M's right is ascending
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
            else: # nums[L] == nums[M], e.g. 1 3 1 1 1, L = 0, M = 2, R = 4, we know that right part will be all 1s
                L += 1
        return False