# 2015-11-10  Runtime: 36 ms
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        start, res = nums[0], []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            if start != nums[i - 1]:
                res.append(str(start) + '->' + str(nums[i - 1]))
            else:
                res.append(str(start))
            start = nums[i]
        # sometimes we can't modify nums
        # if we can modify nums, we can nums.append(sys.maxint)
        # and then we can just return res
        if start != nums[-1]:
            res.append(str(start) + '->' + str(nums[-1]))
        else:
            res.append(str(start))
        return res