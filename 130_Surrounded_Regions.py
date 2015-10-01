# 2015-10-01  Runtime: 148 ms
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        M, N = len(board), len(board[0])
        queue = collections.deque()
        for i in xrange(M):
            if board[i][0] == 'O': queue.append((i, 0))
            if board[i][N - 1] == 'O': queue.append((i, N - 1))
        for j in xrange(N):
            if board[0][j] == 'O': queue.append((0, j))
            if board[M - 1][j] == 'O': queue.append((M - 1, j))
        while queue:
            row, col = queue.popleft()
            if row < 0 or row >= M or col < 0 or col >= N or board[row][col] != 'O':
                continue
            board[row][col] = 'E' # mark it as "edge"
            queue.append((row + 1, col))
            queue.append((row - 1, col))
            queue.append((row, col + 1))
            queue.append((row, col - 1))
        for i in xrange(M):
            for j in xrange(N):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'E': board[i][j] = 'O'