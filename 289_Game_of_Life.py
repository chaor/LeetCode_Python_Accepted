# 2015-12-15  22 tests, 44 ms
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                count = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue
                        if 0 <= i + x < M and 0 <= j + y < N and board[i + x][j + y] & 1 == 1:
                            count += 1
                board[i][j] = (count << 1) + (board[i][j] & 1)
        for i in range(M):
            for j in range(N):
                neighborLiveCount, cellStatus = board[i][j] >> 1, board[i][j] & 1
                if cellStatus == 1:
                    board[i][j] = 1 if neighborLiveCount in (2, 3) else 0
                else:
                    board[i][j] = 1 if neighborLiveCount == 3 else 0