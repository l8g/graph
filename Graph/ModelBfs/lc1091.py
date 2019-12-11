from collections import deque
class Solution:

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        if grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        self._n = n
        self._visited = [[False for _ in range(n)] for _ in range(n)]
        self._order = [[-1 for _ in range(n)] for _ in range(n)]
        self._grid = grid

        self._bfs(0, 0)
        return self._order[n-1][n-1]

    def _bfs(self, x, y):
        self._visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        self._order[x][y] = 1

        while len(queue) > 0:
            curx, cury = queue.popleft()
            for d in Solution.dirs:
                nx, ny = curx + d[0], cury + d[1]
                if self._inArea(nx, ny) and not self._visited[nx][ny] and self._grid[nx][ny] == 0:
                    self._visited[nx][ny] = True
                    self._order[nx][ny] = self._order[curx][cury] + 1
                    queue.append((nx, ny))

    def _inArea(self, x, y):
        return x >= 0 and x < self._n and y >= 0 and y < self._n