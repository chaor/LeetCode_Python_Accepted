# 2015-11-10  Runtime: 64 ms
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # see http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
        count, majority = 0, None
        for x in nums:
            if count:
                count = count + 1 if majority == x else count - 1
            else:
                majority, count = x, 1
        return majority