# 2015-12-12  28 tests, 36 ms
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        liststr = str.split(' ')
        return len(pattern) == len(liststr) and len(set(pattern)) == len(set(liststr)) == len(set(zip(pattern, liststr)))

# 另一种用dictionary的做法，对Word Pattern II有帮助, 28 tests, 44 ms:
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strList, mapper = str.split(' '), {}
        if len(pattern) != len(strList):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapper:
                if strList[i] != mapper[pattern[i]]:
                    return False
            else:
                mapper[pattern[i]] = strList[i]
        return len(mapper) == len(set(mapper.values()))