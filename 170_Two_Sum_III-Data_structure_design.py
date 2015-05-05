# 2015-05-05  Runtime: 191 ms

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        # key is number, value is how many times this number appears
        self.count = {}

    # @return nothing
    def add(self, number):
        self.count[number] = 1 if number not in self.count else self.count[number] + 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for number in self.count:
            if value - number == number:
                if self.count[number] >= 2: return True
            else:
                if value - number in self.count: return True
        return False