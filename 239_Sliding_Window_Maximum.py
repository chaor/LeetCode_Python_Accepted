# 2015-07-18  Runtime: 196 ms
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: return []
        queue = collections.deque(nums[:k])
        queue_max = max(queue)
        res = [queue_max]
        for i in xrange(k, len(nums)):
            poped = queue.popleft()
            queue.append(nums[i])
            if nums[i] > queue_max: queue_max = nums[i]
            elif queue_max == poped: queue_max = max(queue)
            res.append(queue_max)
        return res