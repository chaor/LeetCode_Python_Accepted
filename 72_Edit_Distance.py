# 2015-06-19  Runtime: 272 ms
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        # dp[i][j]表示word1前i个字母变成word2前j个字母的步数(edit distance)
        # if word1[i - 1] == word2[j - 1], then dp[i][j] = dp[i-1][j-1]。如果不等, 则有三种情况，取最小值:
        # 1) 把word1的前i-1个字母变成word2的前j-1个字母, 再把word1的第i个字母换成word2的第j个字母, 即dp[i-1][j-1] + 1
        # 2) 把word1的前i个字母变成word2的前j-1个字母, 再加上word2的第j个字母, 即dp[i][j-1] + 1
        # 3) 删掉word1的第i个字母, 把word1的前i-1个字母变成word2的前j个字母, 即1 + dp[i-1][j]
        
        # initialization
        L1, L2 = len(word1), len(word2)
        dp = [ [0 for j in xrange(L2 + 1)] for i in xrange(L1 + 1) ]
        for k in xrange(1, L1 + 1): dp[k][0] = k 
        for k in xrange(1, L2 + 1): dp[0][k] = k
        
        # dp
        for i in xrange(1, L1 + 1):
            for j in xrange(1, L2 + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else \
                    min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[L1][L2]