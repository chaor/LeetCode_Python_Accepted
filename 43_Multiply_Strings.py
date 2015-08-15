# 2015-08-15  Runtime: 240 ms
class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0': return '0'
        num1, num2 = num1[::-1], num2[::-1]
        res = [0 for i in xrange(len(num1) + len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                res[i + j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
        return ''.join([chr(ord('0') + x) for x in res])[::-1].lstrip('0')