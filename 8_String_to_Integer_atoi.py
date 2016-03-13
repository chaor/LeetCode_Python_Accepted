# 2016-03-13  Runtime: 68 ms
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        try:
            s = s.lstrip() + '$' # remove leading spaces and append an end mark
            for i, ch in enumerate(s):
                if not (ch in '+-' or '0' <= ch <= '9'):
                    result = int(s[:i])
                    return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
        except:
            return 0
