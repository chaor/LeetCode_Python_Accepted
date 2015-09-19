# 2015-09-19  Runtime: 180 ms
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        # thanks to https://leetcode.com/discuss/20240/share-my-dp-solution
        if not matrix: return 0
        m, n, maxRect = len(matrix), len(matrix[0]), 0
        leftEdge, rightEdge, height = [-1] * n, [n] * n, [0] * n
        for i in xrange(m):
            # update height
            for j in xrange(n):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
            # update leftEdge, rightEdge
            currLeftEdge, currRightEdge = -1, n
            for j in xrange(n):
                if matrix[i][j] == '1':
                    leftEdge[j] = max(leftEdge[j], currLeftEdge)
                else:
                    currLeftEdge, leftEdge[j] = j, -1
            for j in reversed(xrange(n)):
                if matrix[i][j] == '1':
                    rightEdge[j] = min(rightEdge[j], currRightEdge)
                else:
                    currRightEdge, rightEdge[j] = j, n
            for j in xrange(n):
                maxRect = max((rightEdge[j] - leftEdge[j] - 1) * height[j], maxRect)
        return maxRect