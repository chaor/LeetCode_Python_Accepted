# 2015-06-10  Runtime: 80 ms
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        # 从右往左找到第一个下降的数，比如是2，然后再从右往左找出比2大的数，比如是5
        # 交换2，5，再对5后面的数列reverse，这样就得到一个高位(2所在的位置)增加后的最小的后续值
        firstAscend = -1
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstAscend = i
                break
        # 如果firstAscend == -1, 则整个nums是降序的，直接reverse就好了
        if firstAscend != -1:
            j = None
            for i in xrange(len(nums) - 1, -1, -1):
                if nums[i] > nums[firstAscend]:
                    j = i
                    break
            nums[firstAscend], nums[j] = nums[j], nums[firstAscend]
        # 对firstAscend位置后面的数进行reverse    
        L, R = firstAscend + 1, len(nums) - 1
        while L < R:
            nums[L], nums[R] = nums[R], nums[L]
            L, R = L + 1, R - 1