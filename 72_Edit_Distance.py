# 2016-03-28   1146 tests, 320 ms
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # initialization
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for i in xrange(len1 + 1)]
        for i in xrange(1, len1 + 1): dp[i][0] = i
        for j in xrange(1, len2 + 1): dp[0][j] = j
        # dp
        for i in xrange(1, len1 + 1):
            for j in xrange(1, len2 + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else dp[i - 1][j - 1] + 1)
        return dp[len1][len2]
