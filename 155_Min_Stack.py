# 2014-12-20  Runtime: 656 ms
class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        # if element is currently minimum, store it in self.minElement
        self.minElement = []
    
    def push(self, x):
        self.stack.append(x)
        if not self.minElement or x <= self.minElement[-1]:
            self.minElement.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            popedElement = self.stack.pop()
            if popedElement == self.minElement[-1]:
                self.minElement.pop()

    # @return an integer
    def top(self):
        return self.stack[-1] if self.stack else None    

    # @return an integer
    def getMin(self):
        return self.minElement[-1] if self.minElement else None