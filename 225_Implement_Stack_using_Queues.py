# 2015-06-10  Runtime: 36 ms
class Stack:
    # initialize your data structure here.
    def __init__(self):
        # Q1 will always keep all elements
        self.Q1, self.Q2, self.stackTop = collections.deque(), collections.deque(), None
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.Q1.append(x)
        self.stackTop = x

    # @return nothing
    def pop(self):
        self.stackTop = None
        for i in xrange(len(self.Q1) - 1):
            self.stackTop = self.Q1.popleft()
            self.Q2.append(self.stackTop)
        self.Q1.popleft()
        self.Q1, self.Q2 = self.Q2, self.Q1

    # @return an integer
    def top(self):
        return self.stackTop

    # @return an boolean
    def empty(self):
        return not self.Q1