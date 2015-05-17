# 2015-05-16  Runtime: 214 ms

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum, diff = None, 10**10  # diff init is infinite
        for i in xrange(len(nums)):
            start, end = 0, len(nums) - 1
            while start < end:
                # make sure i != start, i != end, start != end
                if start == i: start += 1
                if end == i: end -= 1
                if start >= end: continue
                Sum = nums[i] + nums[start] + nums[end]
                if Sum == target:
                    return target
                elif Sum < target:
                    if target - Sum < diff:
                        diff = target - Sum
                        closestSum = Sum
                    start += 1
                else:
                    if Sum - target < diff:
                        diff = Sum - target
                        closestSum = Sum
                    end -= 1
        return closestSum