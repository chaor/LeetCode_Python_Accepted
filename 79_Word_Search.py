# 2015-11-11  Runtime: 364 ms
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if k >= wordLen:
                return True
            if i < 0 or i > M - 1 or j < 0 or j > N - 1:
                return False
            result = False
            if word[k] == board[i][j]:
                board[i][j] = '.'
                if dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or \
                    dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1):
                    result = True
                board[i][j] = word[k] 
            return result
        
        if not board: return False
        if not word: return True
        M, N, wordLen = len(board), len(board[0]), len(word)
        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    return True
        return False