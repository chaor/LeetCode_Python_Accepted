# 2015-06-08  Runtime: 226 ms
class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0': return '0'
        # reverse the two input strings for easier handling
        num1, num2 = num1[::-1], num2[::-1]
        product = [0 for i in xrange(len(num1) + len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                product[i + j] += (ord(num1[i]) - 48) * (ord(num2[j]) - 48) # ord('0') is 48
                product[i + j + 1] += product[i + j] / 10
                product[i + j] %= 10
        # remove leading zeros
        k = len(product) - 1
        while product[k] == 0: k -= 1
        # return result string
        result = []
        for i in xrange(k, -1, -1):
            result.append(chr(48 + product[i]))
        return ''.join(result)