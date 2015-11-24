# 2015-11-23  Runtime: 156 ms
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lCount, rCount = 0, 0
        for ch in s:
            if ch == '(':
                if lCount >= rCount: lCount += 1    
            elif ch == ')':
                if lCount > rCount: rCount += 1
        self.lrCount = min(lCount, rCount)
        self.s, self.lenS, self.result = s, len(s), []
        self.helper(0, 0, 0, '')
        return self.result

    def helper(self, i, L, R, oneAnswer):
        if R > L or L > self.lrCount or R > self.lrCount:
            return
        if i >= self.lenS:
            if L == R == self.lrCount:
                self.result.append(oneAnswer)
            return
        if self.s[i] == '(':
            self.helper(i + 1, L + 1, R, oneAnswer + '(')
            if not oneAnswer or oneAnswer[-1] != '(':
                self.helper(i + 1, L, R, oneAnswer)
        elif self.s[i] == ')':
            self.helper(i + 1, L, R + 1, oneAnswer + ')')
            if not oneAnswer or oneAnswer[-1] != ')':
                self.helper(i + 1, L, R, oneAnswer)
        else:
            self.helper(i + 1, L, R, oneAnswer + self.s[i])