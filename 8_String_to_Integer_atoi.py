# 2015-05-07  Runtime: 79 ms
class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        maxDiv10 = 214748364  # Integer.MAX_VALUE / 10 (Java)
        i, n = 0, len(str)
        while i < n and str[i] == ' ': i += 1
        sign = 1
        if i < n and str[i] == '+': i += 1
        elif i < n and str[i] == '-': sign, i = -1, i + 1
        num = 0
        while i < n and '0' <= str[i] <= '9':
            if num > maxDiv10 or (num == maxDiv10 and int(str[i]) >= 8):
                return 2147483647 if sign == 1 else -2147483648
            num = num * 10 + int(str[i])
            i += 1
        return sign * num
