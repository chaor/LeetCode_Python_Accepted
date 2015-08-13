# 2015-06-18  Runtime: 64 ms
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        char2int = {'0': 0, '1': 1}
        carry, i, j, res = 0, len(a) - 1, len(b) - 1, []
        while i >= 0 or j >= 0 or carry == 1:
            if i >= 0:
                carry += char2int[a[i]]
                i -= 1
            if j >= 0:
                carry += char2int[b[j]]
                j -= 1
            if carry % 2 == 0:
                res.append('0')
            else:
                res.append('1')
            carry /= 2
        return ''.join(res[::-1])