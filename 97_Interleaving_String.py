# 2015-06-25  Runtime: 84 ms
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        # dynamic programming, dp[m][n] True means s3[0...m+n-1] is the interleaving string of s1[0...m-1] and s2[0...n-1]
        # initialization
        dp = [ [False for j in xrange(len(s2) + 1)] for i in xrange(len(s1) + 1)]
        dp[0][0] = True
        for i in xrange(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]
        for i in xrange(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        # dp
        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[len(s1)][len(s2)]