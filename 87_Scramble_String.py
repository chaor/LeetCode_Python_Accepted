# 2015-06-07  Runtime: 80 ms
# thanks to https://leetcode.com/discuss/27231/python-recursive-solution
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        # it's always True for string length <= 3. try 'abc', 'acb', 'bac', 'bca', 'cab', 'cba'
        if len(s1) <= 3:
            return True
        for i in xrange(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
               self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False