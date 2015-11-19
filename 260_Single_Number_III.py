# 2015-11-19  30 tests, 48 ms
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for i in nums: x ^= i
        
        # get the rightmost bit 1 
        mask = 1
        while not mask & x: mask <<= 1
        
        res = [0, 0]
        for i in nums:
            if i & mask:
                res[0] ^= i
            else:
                res[1] ^= i
        return res