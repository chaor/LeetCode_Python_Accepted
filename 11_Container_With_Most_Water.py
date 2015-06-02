# 2015-06-02  Runtime: 100 ms
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