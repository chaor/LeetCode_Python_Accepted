# 2015-06-07  Runtime: 60 ms
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        sign = 1 if dividend > 0 and divisor > 0 or (dividend < 0 and divisor < 0) else -1
        dividend, divisor, quotient = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            n, divisorMultiple = 0, divisor
            while dividend >= divisorMultiple:
                dividend -= divisorMultiple
                quotient += 1 << n
                if quotient > 2147483647: return -2147483648 if sign < 0 else 2147483647
                divisorMultiple <<= 1
                n += 1
        return quotient * sign