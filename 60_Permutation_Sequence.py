# 2015-08-30  Runtime: 44 ms  
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k, res, fac, char = k - 1, '', math.factorial(n - 1), ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:n]
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, fac)
            if i: fac /= i
            res += char.pop(idx)
        return res