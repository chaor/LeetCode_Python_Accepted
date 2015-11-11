# 2015-11-10  Runtime: 56 ms
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        bucket = {} # key is bucketnumber, value is nums[i]
        for i, v in enumerate(nums):
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in bucket and abs(bucket[idx] - v) <= t:
                    return True
            bucket[bucketNum] = v
            if len(bucket) > k:
                del bucket[nums[i - k] / t if t else nums[i - k]]
        return False