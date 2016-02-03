# 2016-02-02  Runtime: 116 ms
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        i, N, diff, closestSum = 0, len(nums), float('inf'), None
        while i < N - 2:
            j, k = i + 1, N - 1
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]
                if Sum == target:
                    return target
                elif Sum < target:
                    if target - Sum < diff:
                        diff, closestSum = target - Sum, Sum
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    j += 1
                else:
                    if Sum - target < diff:
                        diff, closestSum = Sum - target, Sum
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    k -= 1
            while i < N - 2 and nums[i] == nums[i + 1]: i += 1
            i += 1
        return closestSum
