# 2016-03-26  61 tests, 44 ms
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m, n = m - 1, n - 1
        return math.factorial(m + n) / math.factorial(m) / math.factorial(n)
