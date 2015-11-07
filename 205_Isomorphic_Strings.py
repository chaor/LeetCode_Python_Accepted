# 2015-11-07  Runtime: 68 ms
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m1, m2 = [0] * 128, [0] * 128
        for i in range(len(s)):
            si, ti = ord(s[i]), ord(t[i])
            if m1[si] != m2[ti]:
                return False
            m1[si] = i + 1
            m2[ti] = i + 1
        return True