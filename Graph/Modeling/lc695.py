# -*- coding: utf-8 -*-

from collections import deque

class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maxAreaOfIsland(self, grid) -> int:
        self._r = len(grid)
        if self._r == 0:
            return 0
        self._c = len(grid[0])
        if self._c == 0:
            return 0

        self._grid = grid
        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]

        res = 0
        for i in range(self._r):
            for j in range(self._c):
                if not self._visited[i][j] and grid[i][j] == 1:
                    res = max(res, self._bfs(i, j))
        return res

    def _bfs(self, x, y):
        self._visited[x][y] = True
        res = 1
        queue = deque()
        queue.append((x, y))

        while len(queue) > 0:
            curr = queue.popleft()
            for dir in Solution.dirs:
                nextx, nexty = curr[0] + dir[0], curr[1] + dir[1]
                if self._inArea(nextx, nexty) and not self._visited[nextx][nexty] and self._grid[nextx][nexty] == 1:
                    res += 1
                    self._visited[nextx][nexty] = True
                    queue.append((nextx, nexty))
        return res


    def _inArea(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c


s = Solution()
print(s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))

