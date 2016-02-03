# 2016-02-03  Runtime: 40 ms
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return reduce(lambda resultList, digit: [x + y for x in resultList for y in mapping[digit]], digits, [''])
