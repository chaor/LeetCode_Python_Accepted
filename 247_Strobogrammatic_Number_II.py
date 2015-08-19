# 2015-08-18  Runtime: 244 ms
class Solution:
    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic(self, n):
        res = ['0', '1', '8'] if n % 2 else ['']
        while n >= 2:
            n -= 2
            if n < 2:
                res = [a + s + b for a, b in ('11', '88', '69', '96') for s in res]
            else:
                res = [a + s + b for a, b in ('00', '11', '88', '69', '96') for s in res]
        return res