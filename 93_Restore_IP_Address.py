# 2015-05-26  Runtime: 56 ms

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        self.answer, self.oneAnswer = [], []
        self.dfs(s, 0)
        return self.answer
        
    def dfs(self, ip, n):
        if n == 4:
            if ip == '': self.answer.append('.'.join(self.oneAnswer))
            return
        for i in xrange(1, 4):
            if len(ip) >= i: 
                if 0 < int(ip[:i]) <= 255 and ip[:i][0] != '0' or ip[:i] == '0': # avoid '010', but we need to keep '0'
                    self.oneAnswer.append(ip[:i])
                    self.dfs(ip[i:], n + 1)
                    self.oneAnswer.pop()