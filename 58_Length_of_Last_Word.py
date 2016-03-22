# 2016-03-22   59 tests, 40 ms
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_found, letter_start = False, -1
        for i, ch in enumerate(reversed(s)):
            if ch != ' ':
                if not letter_found: letter_start = i
                letter_found = True
            else:
                if letter_found: return i - letter_start
        return len(s) - letter_start if letter_found else 0
