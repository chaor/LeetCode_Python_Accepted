# 2016-02-19  Runtime: 60 ms
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystackPtr, haystackLen, needleLen = 0, len(haystack), len(needle)
        while True:
            needlePtr = 0
            while True:
                if needlePtr == needleLen: return haystackPtr
                if haystackPtr + needlePtr == haystackLen: return -1
                if needle[needlePtr] != haystack[haystackPtr + needlePtr]: break
                needlePtr += 1
            haystackPtr += 1
