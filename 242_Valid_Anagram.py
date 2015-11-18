# 2015-11-17  Runtime: 72 ms
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count = [0] * 256
        for ch in s:
            count[ord(ch)] += 1
        for ch in t:
            if count[ord(ch)] == 0:
                return False
            count[ord(ch)] -= 1
        return True