# 2015-08-09  Runtime: 84 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack, length = [(')', -1)], 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1][0] == '(':
                stack.pop()
                if i - stack[-1][1] > length:
                    length = i - stack[-1][1]
            else:
                stack.append((s[i], i))
        return length