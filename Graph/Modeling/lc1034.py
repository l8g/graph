class Solution:

    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        self._r = len(grid)
        if self._r == 0:
            return grid
        self._c = len(grid[0])
        if self._c == 0:
            return grid

        self._grid = grid
        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]

        self._val = grid[r0][c0]

        self._borders = set()

        self._dfs(r0, c0)

        for (x, y) in self._borders:
            grid[x][y] = color
        return grid



    def _dfs(self, x, y):
        self._visited[x][y] = True

        border = False
        for d in Solution.dirs:
            nx, ny = x + d[0], y + d[1]
            if self._inArea(nx, ny) and self._grid[nx][ny] == self._val:
                if not self._visited[nx][ny]:
                    self._dfs(nx, ny)
            else:
                border = True
        if border:
            self._borders.add((x, y))

    def _inArea(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c






