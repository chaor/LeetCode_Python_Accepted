# 2015-04-16  Runtime: 138 ms

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        num.sort()
        prevNum, res = None, []
        for i in xrange(len(num)):
            if num[i] == prevNum: continue
            prevNum = num[i]
            # num[:i] + num[i+1:] is a copy of num without num[i]
            for subPermutation in self.permuteUnique(num[:i] + num[i+1:]):  
                res.append(subPermutation + [num[i]])
        return res