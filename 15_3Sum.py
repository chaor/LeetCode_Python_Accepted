# 2015-05-16  Runtime: 631 ms

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3: return []
        nums.sort()
        result = set()
        for i in xrange(len(nums)):
            start, end = 0, len(nums) - 1
            while start < end:
                Sum = nums[i] + nums[start] + nums[end]
                if Sum == 0:
                    if start != i and end != i: result.add(tuple(sorted([nums[i], nums[start], nums[end]])))
                    start, end = start + 1, end - 1
                elif Sum < 0:
                    start += 1
                else:
                    end -= 1
        return [list(abc) for abc in result]