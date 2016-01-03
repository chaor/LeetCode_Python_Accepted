# 2016-01-03  # 20 tests, 1672 ms
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: return []
        self.res, self.num, self.target = [], num, target
        self.dfs('', 0, 0, 0)
        return self.res

    def dfs(self, path, i, val, multi):
        if i == len(self.num):
            if self.target == val: self.res.append(path)
            return
        for j in range(i, len(self.num)):
            if j != i and self.num[i] == '0': break
            cur, strCur = int(self.num[i: j + 1]), self.num[i: j + 1]
            if i == 0:
                self.dfs(str(cur), j + 1, cur, cur)
            else:
                self.dfs(path + '+' + strCur, j + 1, val + cur, cur)
                self.dfs(path + '-' + strCur, j + 1, val - cur, -cur)
                self.dfs(path + '*' + strCur, j + 1, val - multi + multi * cur, multi * cur)
