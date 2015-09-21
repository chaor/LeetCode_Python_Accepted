# 2015-09-20  Runtime: 56 ms
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.getIP(s, '', 0)
        return self.result

    def getIP(self, s, IP, k):
        if k == 4:
            if not s: self.result.append(IP[:-1])
            return
        for i in xrange(1, 4):
            if len(s) >= i:
                first_i = s[:i]
                if first_i[0] != '0' and 1 <= int(first_i) <= 255 or first_i == '0':
                    self.getIP(s[i:], IP + first_i + '.', k + 1)