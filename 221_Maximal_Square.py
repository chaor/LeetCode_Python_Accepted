# 2015-07-09  Runtime: 124 ms
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        # thanks to https://leetcode.com/discuss/38614/my-c-code-8ms-dp-o-n-2-time-o-n-space
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        # dp[i][j] is max side length of square whose bottom-right corner is matrix[currRow][j-1]
        dp = [[0 for i in xrange(N + 1)], [0 for i in xrange(N + 1)]]
        maxLen = 0

        for row in xrange(M):
            currRow, prevRow = row % 2, 1 - row % 2
            for col in xrange(1, N + 1):
                if matrix[row][col - 1] == '1':
                    dp[currRow][col] = 1 + min(dp[prevRow][col - 1], dp[currRow][col - 1], dp[prevRow][col])
                    maxLen = max(maxLen, dp[currRow][col])
                else:
                    dp[currRow][col] = 0
        return maxLen * maxLen