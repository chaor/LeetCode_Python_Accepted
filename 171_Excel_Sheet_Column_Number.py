2015-01-08  Runtime: 137 ms

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res, len_s = 0, len(s)
        # e.g. if len_s == 5, we need to count in previous 26, 26^2, 26^3, 26^4
        # 如果s长度为5，那我们需要先加上之前的26, 26^2, 26^3, 26^4
        for i in xrange(1, len_s):
            res += 26 ** i
        # find out the position of s in AAA...A ~ ZZZ...Z (len_s digits)
        # 找到AAA...A~ZZZ...Z(有len_s位)中s的位置
        base = 1
        for one_letter in reversed(s):
            res += (ord(one_letter) - ord('A')) * base
            base *= 26
        return res + 1