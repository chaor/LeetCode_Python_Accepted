# 2015-06-07  Runtime: 60 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        i = 0
        for number in nums:
            if number != val:
                nums[i] = number
                i += 1
        return i