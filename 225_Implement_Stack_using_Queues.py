# 2015-06-10  Runtime: 44 ms
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.Q, self.stackTop = collections.deque(), None
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.Q.append(x)
        self.stackTop = x

    # @return nothing
    def pop(self):
        for i in xrange(len(self.Q) - 1):
            self.stackTop = self.Q.popleft()
            self.Q.append(self.stackTop)
        self.Q.popleft()

    # @return an integer
    def top(self):
        return self.stackTop

    # @return an boolean
    def empty(self):
        return not self.Q