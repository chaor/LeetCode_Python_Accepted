# 2016-01-10  35 tests, 80 ms
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d, Sum, res = {0: -1}, 0, 0
        for i, x in enumerate(nums):
            Sum += x
            res = max(res, i - d.get(Sum - k, i))
            if Sum not in d:
                d[Sum] = i
        return res
