# 2015-12-12  28 tests, 36 ms
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        liststr = str.split(' ')
        return len(pattern) == len(liststr) and len(set(pattern)) == len(set(liststr)) == len(set(zip(pattern, liststr)))