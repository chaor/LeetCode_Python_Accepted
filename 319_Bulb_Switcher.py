# 2015-12-19  35 tests, 56 ms
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bulb i ends up on iff and only if i is a square because it will be switched odd times
        # count how many square numbers
        return int(n ** 0.5)