# 2015-07-29  Runtime: 44 ms
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if not digits: return []
        key = {'0':' ', '2':'abc', '3':'def', '4':'ghi',
               '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = list(key[digits[0]])
        for i in xrange(1, len(digits)):
            result = [x + y for x in result for y in key[digits[i]]]
        return result  