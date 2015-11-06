# 2015-11-05  Runtime: 52 ms
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        # lambda function return a negative number: x < y, 0: x == y, 1: x > y
        nums.sort(cmp = lambda x, y: (x + y < y + x) - (x + y > y + x))
        return ''.join(nums).lstrip('0') or '0'