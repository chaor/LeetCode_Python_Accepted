# 2015-08-02  Runtime: 56 ms
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        a, b, result = abs(dividend), abs(divisor), 0
        while a >= b:
            n, nb = 1, b
            while a >= nb:
                a -= nb
                result += n
                if result >= 2147483648 and sign == -1: return -2147483648
                if result >= 2147483647 and sign == 1: return 2147483647
                n, nb = n << 1, nb << 1
        return sign * result