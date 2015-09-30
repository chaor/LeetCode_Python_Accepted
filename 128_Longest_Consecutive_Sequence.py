# 2015-09-29  Runtime: 44 ms
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # thanks to https://leetcode.com/discuss/18886/my-really-simple-java-o-n-solution-accepted
        d, res = {}, 0  # key is number, value is range length, e.g. [1,2,3,4], d[1] = 4, d[4] = 4
        for x in nums:
            if x in d: continue
            left_length = d[x - 1] if x - 1 in d else 0
            right_length = d[x + 1] if x + 1 in d else 0
            new_length = left_length + 1 + right_length
            d[x] = new_length
            d[x - left_length] = new_length 
            d[x + right_length] = new_length
            res = max(res, new_length)
        return res