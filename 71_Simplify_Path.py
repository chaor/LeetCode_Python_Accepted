# 2015-06-19  Runtime: 60 ms
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        for s in path.split('/'):
            if s in ('.', ''): continue
            if s == '..':
                if stack: stack.pop()
                continue
            stack.append(s)
        return '/' + '/'.join(stack)