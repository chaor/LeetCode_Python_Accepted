# 2015-05-22  Runtime: 36 ms
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        match = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in match: stack.append(char)
            else:
                if not stack or match[stack.pop()] != char: return False
        return not stack # return True is stack is empty