# 2016-03-27  294 tests, 64 ms
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = [ord(ch) - 48 for ch in a[::-1]], [ord(ch) - 48 for ch in b[::-1]]
        carry, result, len_a, len_b = 0, [0] * max(len(a), len(b)), len(a), len(b)
        for i in xrange(max(len_a, len_b)):
            s = carry
            if i < len_a: s += a[i]
            if i < len_b: s += b[i]
            carry, remainder = divmod(s, 2)
            result[i] = chr(remainder + 48)
        if carry: result.append('1')
        return ''.join(result[::-1])
