 # 2015-05-05  Runtime: 70 ms

 class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {} # key is number, value is its index
        for i in xrange(len(nums)):
            if target - nums[i] in dict: return sorted([i + 1, dict[target - nums[i]] + 1])
            dict[nums[i]] = i