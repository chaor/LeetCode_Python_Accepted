# 2015-10-05   Runtime: 44 ms
# thanks to https://leetcode.com/discuss/6632/challenge-me-thx, see woshidaishu's explanation
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for x in nums:
            a = (a ^ x) & b
            b = (b ^ x) | a
        return b