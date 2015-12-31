# 2015-12-30  600 tests, 164 ms
class Solution(object):
    dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(len(self.dp), n + 1):
            self.dp.append(1 + min(self.dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)))
        return self.dp[n]
