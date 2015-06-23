# 2015-06-23  Runtime: 68 ms
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        count = collections.defaultdict(int)
        for i in nums:
            if count[i] >= 1: return True
            count[i] += 1
        return False