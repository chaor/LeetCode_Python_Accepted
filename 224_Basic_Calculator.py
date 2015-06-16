# 2015-06-15  Runtime: 316 ms
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        # thanks to https://leetcode.com/discuss/39532/easy-18-lines-c-16-lines-python
        total, i, sign = 0, 0, [1, 1] # sign has two 1, consider '2 + 3'
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit(): i += 1
                total += sign.pop() * int(s[start:i])
                continue
            if s[i] in '+-(':
                sign.append(sign[-1] * (1, -1)[s[i] == '-'])
            elif s[i] == ')':
                sign.pop()
            i += 1
        return total