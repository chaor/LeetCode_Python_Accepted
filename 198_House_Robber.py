# 2013-03-31  Runtime: 65 ms

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num: 
            return 0
        dp = [0 for i in xrange(len(num) + 1)]
        dp[0], dp[1] = 0, num[0]
        for i in xrange(2, len(num) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + num[i-1])
        return dp[len(num)]