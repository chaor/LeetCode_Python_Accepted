# 2016-03-16, 149 tests, 44 ms
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patch_count, max_reach = 0, 0 # we can form any number in [1, max_reach]
        for x in nums + [float('inf')]:
            while max_reach + 1 < x and max_reach < n:
                # the patch we add is max_reach + 1
                patch_count, max_reach = patch_count + 1, max_reach + max_reach + 1
            if max_reach >= n: return patch_count
            max_reach += x
