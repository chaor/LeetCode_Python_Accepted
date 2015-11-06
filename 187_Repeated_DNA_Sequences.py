# 2015-11-06  Runtime: 108 ms
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10: return []
        tmpSet, resultSet, res = set([]), set([]), []
        for i in range(len(s) - 9):
            DNA = s[i: i + 10]
            if DNA in tmpSet:
                resultSet.add(DNA)
            else:
                tmpSet.add(DNA)
        return list(resultSet)