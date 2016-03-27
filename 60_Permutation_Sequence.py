# 2016-03-26  200 tests, 56 ms
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k, fac, candidate, result = k - 1, math.factorial(n), ['1', '2', '3', '4', '5', '6', '7', '8', '9'][:n], []
        for i in xrange(n, 0, -1):
            fac /= i
            index, k = divmod(k, fac)
            result.append(candidate[index])
            del candidate[index]
        return ''.join(result)
