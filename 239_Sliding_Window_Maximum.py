# 2015-11-16  Runtime: 220 ms
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q, res = collections.deque(), []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                while q[0] <= i - k:
                    q.popleft()
                res.append(nums[q[0]])
        return res