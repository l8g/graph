
class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid) -> int:
        self._r = len(grid)
        if self._r == 0:
            return 0
        self._c = len(grid[0])
        if self._c == 0:
            return 0
        count = 0
        self._grid = grid
        # DFS
        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]
        for i in range(self._r):
            for j in range(self._c):
                if not self._visited[i][j] and grid[i][j] == "1":
                    self._dfs(i, j)
                    count += 1
        return count

    def _dfs(self, i, j):
        self._visited[i][j] = True
        for d in Solution.dirs:
            x, y = d[0] + i, d[1] + j
            if self._inArea(x, y) and not self._visited[x][y] and self._grid[x][y] == "1":
                self._dfs(x, y)

    def _inArea(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c
        
        
s = Solution()
print(s.numIslands([["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]]))