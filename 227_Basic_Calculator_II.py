# 2015-06-24  Runtime: 324 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        self.s, self.i, sign = s, 0, 1
        num, total = self.getNum(), 0
        while self.i < len(self.s):
            if self.s[self.i] in '+-':
                total += num * sign
                sign = 1 if self.s[self.i] == '+' else -1
                self.i += 1
                num = self.getNum()
            elif self.s[self.i] == '*':
                self.i += 1
                num *= self.getNum()
            else:
                self.i += 1
                num = int(num * 1.0 / self.getNum())
        total += num * sign
        return total

    def getNum(self):    
        res = 0
        while self.i < len(self.s):
            if '0' <= self.s[self.i] <= '9':
                res = res * 10 + ord(self.s[self.i]) - ord('0')
            elif self.s[self.i] != ' ':
                return res
            self.i += 1
        return res