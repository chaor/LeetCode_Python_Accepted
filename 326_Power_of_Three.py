# 2016-01-07  21016 tests, 448 ms
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (3 ** 20 % n == 0)
