# 2015-06-23  Runtime: 112 ms
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        # 栈内放非递减的高度的index, 碰到小的height就弹栈，并计算以被弹出的高度为最低高度的矩形面积
        height.append(0)
        i, stack, maxArea = 0, [], 0
        while i < len(height):
            if not stack or height[i] >= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, height[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea