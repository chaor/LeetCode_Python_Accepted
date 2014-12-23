# 2014-12-23  Runtime: 208 ms
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                operand2, operand1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                else:
                    if (operand1 > 0 and operand2 < 0) or (operand1 < 0 and operand2 > 0):
                        stack.append(-(abs(operand1) / abs(operand2)))
                    else:
                        stack.append(operand1 / operand2)
            else:
                stack.append(int(token))
        return stack[0]