# 2015-05-20  Runtime: 112 ms
class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        value = [1000, 900, 500, 400, 100, 90, 50,  40,  10,  9,   5,  4,  1]
        symbol = ['M', 'CM','D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
        roman, i = [], 0
        while num:
            for k in xrange(num / value[i]):
                roman.append(symbol[i])
                num -= value[i]
            i += 1
        return ''.join(roman)