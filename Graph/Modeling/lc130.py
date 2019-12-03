class Solution:

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def solve(self, board) -> None:
        self._r = len(board)
        if self._r < 2:
            return
        self._c = len(board[0])
        if self._c < 2:
            return
        self._board = board
        self.components = set()
        # DFS
        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]
        for i in range(self._r):
            for j in range(self._c):
                if not self._visited[i][j] and board[i][j] == "O":
                    self.components.clear()
                    edge = self._dfs(i, j, self._atEdge(i, j))
                    if not edge:
                        for comp in self.components:
                            board[comp[0]][comp[1]] = "X"

    def _dfs(self, i, j, edge):
        self._visited[i][j] = True
        edge = edge or self._atEdge(i, j)
        self.components.add((i, j))
        
        for d in Solution.dirs:
            nextx, nexty = i + d[0], j + d[1]
            if self._inArea(nextx, nexty) and not self._visited[nextx][nexty] and self._board[nextx][nexty] == "O":
                edge = self._dfs(nextx, nexty, edge) or edge
        return edge



    def _inArea(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c

    def _atEdge(self, x, y):
        return x == 0 or x == self._r - 1 or y == 0 or y == self._c - 1;

s = Solution()
b = [["X","O","X","O","X","O","O","O","X","O"],
     ["X","O","O","X","X","X","O","O","O","X"],
     ["O","O","O","O","O","O","O","O","X","X"],
     ["O","O","O","O","O","O","X","O","O","X"],
     ["O","O","X","X","O","X","X","O","O","O"],
     ["X","O","O","X","X","X","O","X","X","O"],
     ["X","O","X","O","O","X","X","O","X","O"],
     ["X","X","O","X","X","O","X","O","O","X"],
     ["O","O","O","O","X","O","X","O","X","O"],
     ["X","X","O","X","X","X","X","O","O","O"]]

c = [["X","O","X","O","X","O","O","O","X","O"],
     ["X","O","O","X","X","X","O","O","O","X"],
     ["O","O","O","O","O","O","O","O","X","X"],
     ["O","O","O","O","O","O","X","O","O","X"],
     ["O","O","X","X","O","X","X","O","O","O"],
     ["X","O","O","X","X","X","X","X","X","O"],
     ["X","O","X","X","X","X","X","O","X","O"],
     ["X","X","O","X","X","X","X","O","X","X"],
     ["O","O","O","X","X","X","X","O","X","O"],
     ["X","X","O","X","X","X","X","O","O","O"]]

d = [["X","O","X","O","X","O","O","O","X","O"],
     ["X","O","O","X","X","X","O","O","O","X"],
     ["O","O","O","O","O","O","O","O","X","X"],
     ["O","O","O","O","O","O","X","O","O","X"],
     ["O","O","X","X","O","X","X","O","O","O"],
     ["X","O","O","X","X","X","X","X","X","O"],
     ["X","O","X","X","X","X","X","O","X","O"],
     ["X","X","O","X","X","X","X","O","O","X"],
     ["O","O","O","v","X","X","X","O","X","O"],
     ["X","X","O","X","X","X","X","O","O","O"]]

s.solve(b)
print(b)
