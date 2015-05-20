# 2015-05-20  Runtime: 236 ms
class MinStack:
    def __init__(self):
        self.stack, self.minStack = [], []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]: self.minStack.append(x)

    # @return nothing
    def pop(self):
        if self.stack.pop() == self.minStack[-1]: self.minStack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minStack[-1]