# 2015-03-01  Runtime: 223 ms

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        for i in xrange(k):
            nums.insert(0, nums.pop()) 