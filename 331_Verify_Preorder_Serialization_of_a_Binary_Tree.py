# 2016-04-03  150 tests, 80 ms
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for value in preorder.split(','):
            if value == '#':
                while len(stack) >= 2 and stack[-1] == '#' and stack[-2] != '#':
                    stack.pop()
                    stack.pop()
            stack.append(value)
        return stack == ['#']
