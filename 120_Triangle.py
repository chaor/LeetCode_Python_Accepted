# 2015-03-23  Runtime: 72 ms

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        upper_level_dp = [None for k in xrange(len(triangle))]
        upper_level_dp[0] = triangle[0][0]
        dp = upper_level_dp[:]
        for row in triangle:
            if len(row) == 1: continue
            dp[0] = upper_level_dp[0] + row[0]
            for i in xrange(1, len(row)-1):
                dp[i] = row[i] + min(upper_level_dp[i], upper_level_dp[i-1])
            dp[len(row)-1] = row[-1] + upper_level_dp[len(row)-2]
            upper_level_dp = dp[:]
        return min(dp)