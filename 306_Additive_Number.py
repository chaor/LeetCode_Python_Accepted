# 2016-01-05  36 tests, 48 ms
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if (len(a) == 1 or a[0] != '0') and (len(b) == 1 or b[0] != '0'):
                c = str(int(a) + int(b))
                while j < n and num.startswith(c, j):
                    j += len(c)
                    a, b = b, c
                    c = str(int(a) + int(b))
                if j == n:
                    return True
        return False
