# 2015-05-06  Runtime: 139 ms

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        haystackPtr = 0
        while True: # traverse haystack
            needlePtr = 0
            while True: # traverse needle
                if needlePtr == len(needle): return haystackPtr
                if haystackPtr + needlePtr == len(haystack): return -1
                if needle[needlePtr] != haystack[haystackPtr + needlePtr]: break
                needlePtr += 1
            haystackPtr += 1