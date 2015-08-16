# 2015-08-16  Runtime: 60 ms
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        # https://en.wikipedia.org/wiki/Digital_root
        # digital root == repeated digital sum == n - largest multiple of 9 less than n
        # can be used to calculate mod, also dr(dr(x) + dr(y)) == dr(x + y)
        return num - (num - 1) / 9 * 9 if num else 0