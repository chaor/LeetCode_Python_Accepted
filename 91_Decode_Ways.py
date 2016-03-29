# 2016-03-28   259 tests, 64 ms
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        len_s = len(s)
        dp = [1] + [0] * len_s
        for i in xrange(1, len_s + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len_s]
