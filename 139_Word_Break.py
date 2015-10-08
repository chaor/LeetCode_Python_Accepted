# 2015-10-08  Runtime: 40 ms
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s: return True
        if not wordDict: return False
        minLen, maxLen, lenS = len(min(wordDict, key = len)), len(max(wordDict, key = len)), len(s)
        # dp[i] == True means first i letters of s can be segmented
        dp = [False] * (lenS + 1)
        dp[0] = True
        for i in xrange(lenS + 1 - minLen):
            if dp[i]:
                for j in xrange(minLen, maxLen + 1):
                    if i + j > lenS: break
                    if s[i: i + j] in wordDict: dp[i + j] = True
        return dp[lenS]