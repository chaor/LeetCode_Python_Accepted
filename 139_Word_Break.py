# 2015-02-02  Runtime: 40 ms

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not dict: return False
        
        # dp[i] == True means first i letters of s can be segmented
        dp = [False for i in xrange(len(s) + 1)]
        dp[0] = True
        maxDictWordLen = len(max(dict, key = len))
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, maxDictWordLen + 1):
                if i >= j:
                    if dp[i - j] and s[i-j:i] in dict:
                        dp[i] = True
        return dp[len(s)]