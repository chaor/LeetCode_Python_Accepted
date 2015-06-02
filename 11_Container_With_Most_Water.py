# 2015-06-02  Runtime: 100 ms

# O(N)解法，two pointers, height[L]和height[R]谁小就移动相应的指针
# 比如n = 6, L = 0, R = 5, 已算line 0和line 5围成的面积，即(0,5)，
# 如果发现height[0] < height[5], 就没有必要再算(0,4), (0,3), (0,2)和(0,1)
# 因为它们围成的面积更小，所以可以直接移动L了。

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        L, R, maxArea = 0, len(height) - 1, 0
        while L < R:
            maxArea = max(maxArea, (R - L) * min(height[L], height[R]))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxArea