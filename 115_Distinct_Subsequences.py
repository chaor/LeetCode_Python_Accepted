# 2015-04-14  Runtime: 188 ms

class Solution:
    # @param S, a string
    # @param T, a string
    # @return an integer
    def numDistinct(self, S, T):
        # dp[m][n] is number of distince subsequences of first m letters of T in first n letters of S
        dp = [[0 for x in xrange(len(S) + 1)] for y in xrange(len(T) + 1)]
        # dp[0][*] = 1 because empty string is subsequence of any string
        for i in xrange(len(S) + 1): dp[0][i] = 1 
        # outer loop scans T, inner loop scans S
        # for inner loop, start from the same length place with outer loop
        for i in xrange(1, len(T) + 1):
            for j in xrange(i, len(S) + 1):
                dp[i][j] = dp[i][j-1] if T[i-1] != S[j-1] else dp[i-1][j-1] + dp[i][j-1]
        return dp[len(T)][len(S)]