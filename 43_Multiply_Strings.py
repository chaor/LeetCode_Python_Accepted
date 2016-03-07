# 2016-03-07  311 tests, 180 ms
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': return '0'
        a, b, len_a, len_b = [ord(i) - 48 for i in num1[::-1]], [ord(j) - 48 for j in num2[::-1]], len(num1), len(num2)
        res = [0] * (len_a + len_b)
        for i in xrange(len_a):
            for j in xrange(len_b):
                res[i + j] += a[i] * b[j]
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
        return ''.join([chr(48 + x) for x in res])[::-1].lstrip('0')
