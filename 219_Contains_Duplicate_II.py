# 2015-06-23  Runtime: 72 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        s = set()
        for i in xrange(len(nums)):
            if i > k: s.remove(nums[i - k - 1])
            if nums[i] in s: return True
            s.add(nums[i])
        return False