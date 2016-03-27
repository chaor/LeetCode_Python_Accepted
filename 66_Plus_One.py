# 2016-03-27  108 tests, 40 ms
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i, d in enumerate(reversed(digits), start = 1):
            if d < 9:
                digits[-i] += 1
                return digits
            else:
                digits[-i] = 0
        return [1] + digits
