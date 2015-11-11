# 2015-11-10  Runtime: 128 ms
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)] # used to record side length of largest square
        maxSideLength = 0 
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    maxSideLength = max(maxSideLength, dp[i][j])
        return maxSideLength ** 2