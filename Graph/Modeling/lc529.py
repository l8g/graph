class Solution:

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def updateBoard(self, board, click):
        self._r = len(board)
        if self._r == 0:
            return board
        self._c = len(board[0])
        if self._c == 0:
            return board

        self._board = board
        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]

        x, y = click[0], click[1]

        if board[x][y] == "M":
            board[x][y] = "X"
            return board

        self._dfs(x, y)

        return board

    def _dfs(self, x, y):
        self._visited[x][y] = True

        count = 0
        for d in Solution.dirs:
            nx, ny = x + d[0], y + d[1]
            if self._inArea(nx, ny):
                val = self._board[nx][ny]
                if val == "M" or val == "X":
                    count += 1
        if count > 0:
            self._board[x][y] = str(count)
        else:
            self._board[x][y] = "B"
            for d in Solution.dirs:
                nx, ny = x + d[0], y + d[1]
                if self._inArea(nx, ny) and not self._visited[nx][ny] and self._board[nx][ny] == "E":
                    self._dfs(nx, ny)

    
    def _inArea(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c


s = Solution()

print(s.updateBoard([["E","E","E","E","E"],
                     ["E","E","M","E","E"],
                     ["E","E","E","E","E"],
                     ["E","E","E","E","E"]],[3,0]))