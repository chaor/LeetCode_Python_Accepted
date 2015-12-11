# 2015-12-11  25 tests, 44 ms
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i] + '--' + s[i + 2:] for i in range(len(s) - 1) if s[i:i + 2] == '++']