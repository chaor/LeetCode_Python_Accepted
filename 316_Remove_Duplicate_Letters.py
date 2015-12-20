# 2015-12-20   286 tests, 88 ms
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_s = set(s)
        for ch in sorted(set_s):
            suffix = s[s.index(ch):]
            if set(suffix) == set_s:
                return ch + self.removeDuplicateLetters(suffix.replace(ch, ''))
        return ''