# 2015-03-27  Runtime: 248 ms  BFS

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return
        rowNum, colNum = len(board), len(board[0])
        visited = [[False for j in xrange(colNum)] for i in xrange(rowNum)]
        Q = collections.deque()
        for i in xrange(rowNum):
            if board[i][0] == 'O': Q.append((i,0))
            if board[i][colNum - 1] == 'O': Q.append((i, colNum - 1))
        for i in xrange(colNum):
            if board[0][i] == 'O': Q.append((0, i))
            if board[rowNum - 1][i] == 'O': Q.append((rowNum - 1, i))
        while Q:
            cur = Q.popleft()
            board[cur[0]][cur[1]] = 'E' # mark 'O' on the edge as 'E'
            visited[cur[0]][cur[1]] = True
            if cur[0] > 0 and not visited[cur[0] - 1][cur[1]] and board[cur[0] - 1][cur[1]] == 'O':
                Q.append((cur[0] - 1, cur[1]))
            if cur[0] < rowNum - 1 and not visited[cur[0] + 1][cur[1]] and board[cur[0] + 1][cur[1]] == 'O':
                Q.append((cur[0] + 1, cur[1]))
            if cur[1] > 0 and not visited[cur[0]][cur[1] - 1] and board[cur[0]][cur[1] - 1] == 'O':
                Q.append((cur[0], cur[1] - 1))
            if cur[1] < colNum - 1 and not visited[cur[0]][cur[1] + 1] and board[cur[0]][cur[1] + 1] == 'O':
                Q.append((cur[0], cur[1] + 1))
        for i in xrange(rowNum):
            for j in xrange(colNum):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == 'E': board[i][j] = 'O'