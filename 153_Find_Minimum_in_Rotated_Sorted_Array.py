# 2015-05-28  Runtime: 48 ms 
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        # draw a x-y graph and it can help to determine the next L or R value
        L, R = 0, len(nums) - 1
        while L < R and nums[L] > nums[R]:
            M = (L + R) / 2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]