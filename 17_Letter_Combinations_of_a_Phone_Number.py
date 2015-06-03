# 2015-06-02  Runtime: 44 ms
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits: return []
        self.d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        self.digits, self.result = digits, []
        self.dfs(0, [])
        return self.result
        
    def dfs(self, i, L):
        if i == len(self.digits):
            self.result.append(''.join(L))
            return
        for letter in self.d[self.digits[i]]:
            self.dfs(i + 1, L + [letter])