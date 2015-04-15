# 2015-04-15 Runtime: 99 ms  

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.res, self.num = [], num
        self.recursive(0)
        return self.res
        
    def recursive(self, beginPos):
        if beginPos >= len(self.num):
            # # put the copy of self.num into self.res, otherwise everything in self.res will be the same
            self.res.append(self.num[:]) 
            return
        # fix self.num[0 ... beginPos-1], permute self.num[beginPos ... end]
        for i in xrange(beginPos, len(self.num)):
            self.num[i], self.num[beginPos] = self.num[beginPos], self.num[i]
            self.recursive(beginPos + 1)
            self.num[beginPos], self.num[i] = self.num[i], self.num[beginPos]