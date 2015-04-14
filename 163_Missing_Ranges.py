# 2016-04-04  Runtime: 50 ms

class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        A.append(upper + 1)
        res = []
        prev = lower - 1
        for i in A:
            if i == prev + 2:
                res.append(str(i - 1))
            elif i > prev + 2:
                res.append(str(prev + 1) + '->' + str(i - 1))
            prev = i
        return res