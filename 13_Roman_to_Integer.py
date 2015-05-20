# 2015-05-20  Runtime: 148 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # for 'MCD', M 1000, C 100, we have 1100, then we meet 'D', so we need to subtrace two C (200)
        prev, result = 0, 0
        for symbol in s:
            result += d[symbol]
            if prev < d[symbol]: result -= 2 * prev
            prev = d[symbol]
        return result