# 2015-07-28  Runtime: 308 ms

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
    	# thanks to https://leetcode.com/discuss/23638/concise-o-n-2-java-solution
        nums.sort()
        result = []
        # ia, ib, ic is the index of the a,b,c, a <= b <= c
        for ia in xrange(len(nums) - 2):
            # remove duplicated a
            if ia == 0 or (ia > 0 and nums[ia] != nums[ia - 1]):
                ib, ic = ia + 1, len(nums) - 1
                while ib < ic:
                    if nums[ia] + nums[ib] + nums[ic] == 0:
                        result.append([nums[ia], nums[ib], nums[ic]])
                        # remove duplicated b, c
                        while ib < ic and nums[ib] == nums[ib + 1]: ib += 1
                        while ib < ic and nums[ic] == nums[ic - 1]: ic -= 1
                        ib, ic = ib + 1, ic - 1
                    elif nums[ia] + nums[ib] + nums[ic] < 0:
                        ib += 1
                    else:
                        ic -= 1
        return result