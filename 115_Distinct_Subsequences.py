# 2015-08-30  63 tests, 132 ms
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Let dp[i][j] be number of distinct subsequences for first i letters of s, first j letters of t
        # if s[i - 1] != t[j - 1], then dp[i][j] = dp[i - 1][j]
        # if s[i - 1] == t[j - 1], then dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        # based on this, we can just use one-dimension dp array: 
        # len(dp) = len(t) + 1, dp[0] = 1
        # if s[i - 1] == t[j - 1], then dp[j] = dp[j] + dp[j - 1],  1 <= j <= len(t)
        lenS, lenT = len(s), len(t)
        dp = [0 for i in xrange(lenT + 1)]
        dp[0] = 1
        for i in xrange(lenS):
            for j in reversed(xrange(1, lenT + 1)):
                if s[i] == t[j - 1]:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[lenT]