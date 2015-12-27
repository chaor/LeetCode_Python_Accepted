# 2015-12-27  24 tests, 44 ms
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.charNum, start, start_length, self.length = {}, '', 1, len(s)
        for ch in s:
            self.charNum[ch] = self.charNum.get(ch, 0) + 1
        for ch in self.charNum:
            if self.charNum[ch] % 2:
                if start: return []
                start, start_length = ch, 1
                self.charNum[ch] -= 1
        self.res = []
        self.dfs(start, start_length)
        return self.res

    def dfs(self, cur, cur_length):
        if cur_length == self.length:
            self.res.append(cur)
            return
        for ch in self.charNum:
            if self.charNum[ch] > 0:
                self.charNum[ch] -= 2
                self.dfs(ch + cur + ch, cur_length + 2)
                self.charNum[ch] += 2
