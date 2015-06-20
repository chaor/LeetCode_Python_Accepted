# 2015-06-19  Runtime: 256 ms
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        if len(t) == 0 or len(s) < len(t): return ''
        require = {i: 0 for i in string.uppercase + string.lowercase + '_'}
        for char in t: require[char] += 1

        start, count, minIndex, minLen = 0, 0, 0, 10 ** 10 # infinity
        for end in xrange(len(s)):
            require[s[end]] -= 1
            if require[s[end]] >= 0: count += 1
            while count == len(t):
                if end - start + 1 < minLen:
                    minLen, minIndex = end - start + 1, start
                require[s[start]] += 1
                if require[s[start]] > 0: count -= 1
                start += 1

        if minLen == 10 ** 10: return ''
        return s[minIndex:minIndex + minLen]