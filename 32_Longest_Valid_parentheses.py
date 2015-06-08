# 2015-06-08  Runtime: 88 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        # 记录左括号的index，每次出现右括号且可以跟栈顶左括号匹配时，更新一下maxLen
        stack, maxLen = [-1], 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1])
            else:
                stack.append(i)
        return maxLen