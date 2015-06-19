# 2015-06-18  Runtime: 96 ms
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        # thanks to https://leetcode.com/discuss/18970/concise-recursive-and-dp-solutions-with-full-explanation-in
        # dp[m][n] True means s[0...m-1] can be matched by p[0...n-1]
        dp = [[False for j in xrange(len(p) + 1)] for i in xrange(len(s) + 1)]
        dp[0][0] = True
        # when s is empty
        for i in xrange(2, len(p) + 1): dp[0][i] = p[i - 1] == '*' and dp[0][i - 2]
        # when p is empty, always False
            
        # start dp
        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] == '*': # '*' can match 0 time, or >= 1 letters in s
                    dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], '.') and dp[i - 1][j])
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '.') and dp[i - 1][j - 1]
        return dp[len(s)][len(p)]