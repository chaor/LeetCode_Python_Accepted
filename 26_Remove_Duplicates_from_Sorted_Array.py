# 2016-02-09  Runtime: 96 ms
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length, slow = len(nums), 0
        if length <= 1: return length
        for fast in range(length):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
