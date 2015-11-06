# 2015-11-06  Runtime: 84 ms
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums.reverse()
        # reverse the first half
        self.reverse(nums, 0, k - 1)
        # reverse the second half
        self.reverse(nums, k, n - 1)
            
    def reverse(self, nums, L, R):
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
            R -= 1