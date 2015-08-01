# 2015-08-01  Runtime: 52 ms
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        # thanks to https://leetcode.com/discuss/43122/4-7-lines-python
        def gen(L, R, s):
            # L, R is available left/right parenthesis number
            if R >= L >= 0:
                if R == 0: self.result.append(s)
                gen(L - 1, R, s + '(')
                gen(L, R - 1, s + ')')
        self.result = []
        gen(n, n, '')
        return self.result