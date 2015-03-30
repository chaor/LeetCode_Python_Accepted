# 2015-03-29  Runtime: 736 ms

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lenS = len(s)
        isPal = [[False for j in xrange(lenS)] for i in xrange(lenS)]
        minPalNum = [i + 1 for i in xrange(lenS)]
        for j in xrange(lenS):
            for i in reversed(xrange(j + 1)):
                if s[i] == s[j] and (j - i <= 1 or isPal[i+1][j-1]):
                    isPal[i][j] = True
                    minPalNum[j] = min(minPalNum[j], minPalNum[i - 1] + 1 if i >= 1 else 1)
        return minPalNum[lenS - 1] - 1