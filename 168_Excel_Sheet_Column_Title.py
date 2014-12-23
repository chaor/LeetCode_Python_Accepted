# 2014-12-20  Runtime: 152 ms
class Solution:
    # @return a string
    def convertToTitle(self, num):
        # It's not just base 10 to base 26, 不是简单的10进制转26进制
        # A ~ Z, 26 numbers, AA ~ ZZ, 26^2 numbers, AAA ~ ZZZ, 26^3 numbers, ...
        range, digit = 26, 1
        while num > range:
            num, digit = num - range, digit + 1
            range *= 26
        num -= 1
        
        # now base 10 to base 26, 现在知道了结果有几位，可以10进制转26进制了
        res = []
        for i in xrange(digit):
            res.append(chr(ord('A') + num % 26))
            num /= 26
        return ''.join(res[::-1])