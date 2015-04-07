# 2015-04-06  Runtime: 62 ms

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.res = []
        self.dfs(s, 0, '')
        return self.res
        
    def dfs(self, s, level, oneAnswer):
        if level > 4: 
            return
        if level == 4:
            if not s: self.res.append(oneAnswer[:-1]) # remove the last '.'
            return
        for i in xrange(1, 4):
            # s[:i] == str(int(s[:i])) will remove leading zeros, for '010010', we don't want '01.0.0.10'
            if len(s) >= i and 0 <= int(s[:i]) <= 255 and s[:i] == str(int(s[:i])):
                self.dfs(s[i:], level + 1, oneAnswer + s[:i] + '.')