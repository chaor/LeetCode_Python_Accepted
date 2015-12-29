# 2015-12-28  102 tests, 456 ms
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # thanks to https://leetcode.com/discuss/75804/short-python-ruby-c
        def top_k(nums, k):
            drop, res = len(nums) - k, []
            for x in nums:
                while drop and res and res[-1] < x:
                    drop -= 1
                    res.pop()
                res.append(x)
            return res[:k]

        def merge(a, b):
            a, b = collections.deque(a), collections.deque(b)
            return [max(a, b).popleft() for i in range(len(a) + len(b))]

        return max(merge(top_k(nums1, i), top_k(nums2, k - i))
            for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))
