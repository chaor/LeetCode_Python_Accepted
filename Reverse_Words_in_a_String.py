# 2014-12-23  Runtime: 92 ms
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # if L is a list, L[::-1] can reverse it
        # L[::-1]可以翻转L这个list
        return ' '.join(s.split()[::-1])