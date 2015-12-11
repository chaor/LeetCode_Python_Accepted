# 2015-12-11  33 tests, 288 ms
class Solution(object):
    d = {}
    
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # thanks to https://leetcode.com/discuss/64357/memoization-3150ms-130ms-44ms-python
        if s not in self.d:
            self.d[s] = any([s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:]) for i in range(len(s))])
        return self.d[s]