# 2015-06-18  Runtime: 60 ms
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        char2int = {'0': 0, '1': 1}
        i, j, carry, res = len(a) - 1, len(b) - 1, 0, []
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += char2int[a[i]]
                i -= 1
            if j >= 0:
                carry += char2int[b[j]]
                j -= 1
            res.append(chr(carry % 2 + 48))
            carry /= 2
        return ''.join(res[::-1])