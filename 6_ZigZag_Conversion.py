# 2015-05-30  Runtime: 124 ms
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1: return s
        # 把abcd...xyz写成W型就容易找到规律了，每行有两个gap
        # 分别是2(n-1)和2x0, 2(n-2)和2x1, 2(n-3)和2x2,...2x0和2(n-1)
        result, lineStart = [], -1
        for i in xrange(numRows):
            lineStart += 1
            if lineStart >= len(s): break
            result.append(s[lineStart])
            k, gap1, gap2 = lineStart, 2 * (numRows - 1 - i), 2 * i
            while True:
                if gap1 > 0:
                    k += gap1
                    if k >= len(s): break
                    result.append(s[k])
                if gap2 > 0:
                    k += gap2
                    if k >= len(s): break
                    result.append(s[k])
        return ''.join(result)