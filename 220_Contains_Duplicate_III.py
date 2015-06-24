# 2015-06-23  Runtime: 124 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # thanks to https://leetcode.com/discuss/38176/python-ordereddict
        if k <= 0 or t < 0: return False
        d = collections.OrderedDict()
        for number in nums:
            key = number if t == 0 else number // t
            for value in (d.get(key - 1), d.get(key), d.get(key + 1)):
                if value is not None and abs(value - number) <= t: return True
            if len(d) == k: d.popitem(last = False) # pop from head
            d[key] = number
        return False