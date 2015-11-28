# 2015-11-27  23 tests, 56 ms
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strings:
            key = tuple((ord(s[i + 1]) - ord(s[i])) % 26 for i in range(len(s) - 1))
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        return [sorted(i) for i in d.values()]