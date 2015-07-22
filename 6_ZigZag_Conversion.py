# 2015-07-21  Runtime: 148 ms
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        # thanks to https://leetcode.com/discuss/10493/easy-to-understand-java-solution
        line = [[] for i in xrange(numRows)]
        i = 0
        while i < len(s):
            j = 0  # go down
            while j < numRows and i < len(s):
                line[j].append(s[i])
                i += 1
                j += 1
            j = numRows - 2  # go up
            while j >= 1 and i < len(s):
                line[j].append(s[i])
                i += 1
                j -= 1
        result = ''
        for i in xrange(numRows):
            result += ''.join(line[i])
        return result