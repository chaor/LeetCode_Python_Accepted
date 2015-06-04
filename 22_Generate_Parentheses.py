# 2015-06-04  Runtime: 72 ms
# thanks to https://leetcode.com/discuss/14436/concise-recursive-c-solution
class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        self.result = []
        self.dfs([], n, 0)
        return self.result
        
    def dfs(self, L, remainingLeftParen, remainingRightParen):
        if remainingLeftParen == remainingRightParen == 0:
            self.result.append(''.join(L))
            return
        if remainingLeftParen > 0: self.dfs(L + ['('], remainingLeftParen - 1, remainingRightParen + 1)
        if remainingRightParen > 0: self.dfs(L + [')'], remainingLeftParen, remainingRightParen - 1)