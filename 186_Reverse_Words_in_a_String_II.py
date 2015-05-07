# 2015-05-07  Runtime: 103 ms
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        # reverse the entire s
        for i in xrange(len(s) / 2): 
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        # then reverse each word
        wordBeginPtr, wordEndPtr = 0, 0
        while wordEndPtr <= len(s):
            if wordEndPtr == len(s) or s[wordEndPtr] == ' ':
                for i in xrange((wordEndPtr - wordBeginPtr) / 2):
                    s[wordBeginPtr + i], s[wordEndPtr - 1 - i] = s[wordEndPtr - 1 - i], s[wordBeginPtr + i]
                wordBeginPtr = wordEndPtr + 1
            wordEndPtr += 1