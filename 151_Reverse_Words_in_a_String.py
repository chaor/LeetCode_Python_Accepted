# 2014-12-23  Runtime: 92 ms
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # if L is a list, L[::-1] can reverse it
        # L[::-1]可以翻转L这个list
        return ' '.join(s.split()[::-1])


# 2015-05-06  Runtime: 71 ms, O(n) runtime, O(n) space
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        wordEndPtr, result = len(s), []
        for i in reversed(xrange(len(s))):
            if s[i] == ' ': 
                wordEndPtr = i
            elif i == 0 or s[i - 1] == ' ':
                if result: result.append(' ')
                result.append(s[i:wordEndPtr])
        return ''.join(result)