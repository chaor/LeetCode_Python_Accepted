# 2015-06-27  Runtime: 48 ms
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        # thanks to https://leetcode.com/discuss/36770/0ms-easy-to-understand-c-solution
        def robHelper(nums, L, R):
            if L == R: return nums[L]
            money = [0 for i in xrange(R - L + 1)]
            money[0], money[1] = nums[L], max(nums[L], nums[L + 1])
            for i in xrange(2, R - L + 1):
                money[i] = max(money[i - 1], money[i - 2] + nums[L + i])
            return money[R - L]
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(robHelper(nums, 0, len(nums) - 2), robHelper(nums, 1, len(nums) - 1))