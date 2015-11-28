# 2015-11-27  62 tests, Runtime: 344 ms

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # initialize the queue
        if not rooms:
            return
        INF, m, n = 2147483647, len(rooms), len(rooms[0])
        queue = collections.deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
                    
        # BFS
        dirdat = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while queue:
            i, j = queue.popleft()
            for dx, dy in dirdat:
                if 0 <= i + dx < m and 0 <= j + dy < n and rooms[i + dx][j + dy] == INF:
                    rooms[i + dx][j + dy] = rooms[i][j] + 1
                    queue.append((i + dx, j + dy))