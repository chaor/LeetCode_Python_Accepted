# 2014-12-18, Runtime: 140 ms
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1List = [int(x) for x in version1.split('.')]
        v2List = [int(x) for x in version2.split('.')]
        len1, len2 = len(v1List), len(v2List)
        listDiff = [0 for i in xrange(abs(len1 - len2))]
        # add [0, 0, 0, ...] to the shorter list to match the longer one
        # 向较短的list里补充[0, 0, 0, ...]使两个list一样长
        if len1 > len2:
            v2List.extend(listDiff)
        else:
            v1List.extend(listDiff)
        # Python list comparison is like Lexicographical
        # Python list的比较遵循字典序
        return 1 if v1List > v2List else (-1 if v1List < v2List else 0)