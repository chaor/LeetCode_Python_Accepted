# 2015-06-22  Runtime: 160 ms
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        # thanks to https://leetcode.com/discuss/20240/share-my-dp-solution
        if not matrix: return 0
        m, n, maxArea = len(matrix), len(matrix[0]), 0
        L_border, R_border, h = \
                [0 for i in xrange(n)], [n - 1 for i in xrange(n)], [0 for i in xrange(n)]
        for i in xrange(m):
            curr_L_border, curr_R_border = 0, n - 1
            for j in xrange(n):
                h[j] = h[j] + 1 if matrix[i][j] == '1' else 0
            for j in xrange(n):
                if matrix[i][j] == '1': 
                    L_border[j] = max(L_border[j], curr_L_border)
                else:
                    L_border[j], curr_L_border = 0, j + 1
            for j in reversed(xrange(n)):
                if matrix[i][j] == '1':
                    R_border[j] = min(R_border[j], curr_R_border)
                else:
                    R_border[j], curr_R_border = n - 1, j - 1
            for j in xrange(n):
                maxArea = max(maxArea, (R_border[j] - L_border[j] + 1) * h[j])
        return maxArea