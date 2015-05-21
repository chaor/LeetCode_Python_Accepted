# 2015-05-20  Runtime: 64 ms
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        calc = {'+':lambda x, y: x + y, '-':lambda x, y: x - y, '*':lambda x, y: x * y, \
                '/':lambda x, y: -(x / -y) if (x > 0 and y < 0) else -(-x / y) if (x < 0 and y > 0) else x / y}
        stack = []
        for token in tokens:
            if token not in calc:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(calc[token](x,y))
        return stack[0]