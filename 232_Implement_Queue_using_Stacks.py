# 2015-07-07  Runtime: 48 ms
class Queue:
    # initialize your data structure here.
    def __init__(self):
        # there will always be 0 or 1 element in stack s1
        self.s1, self.s2 = [], []
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        if not self.s1:
            self.s1.append(x)
        else:
            self.s2.append(x)
            
    # @return nothing
    def pop(self):
        self.s1.pop()
        while len(self.s2) > 1:
            self.s1.append(self.s2.pop())
        self.s1, self.s2 = self.s2, self.s1

    # @return an integer
    def peek(self):
        return self.s1[-1]

    # @return an boolean
    def empty(self):
        return not self.s1