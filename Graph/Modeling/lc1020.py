class Solution:

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numEnclaves(self, A) -> int:
        self._r = len(A)
        if self._r == 0:
            return 0
        self._c = len(A[0])
        if self._c == 0:
            return 0

        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]
        self._A = A
        count = 0
        for i in range(self._r):
            for j in range(self._c):
                if not self._visited[i][j] and A[i][j] == 1:
                    count += self._dfs(i, j)
        return count

    def _dfs(self, i, j):
        self._visited[i][j] = True

        count = 0 if self._atEdge(i, j) else 1
        for d in Solution.dirs:
            nx, ny = i + d[0], j + d[1]
            if self._inArea(nx, ny) and not self._visited[nx][ny] and self._A[nx][ny] == 1:
                childCount = self._dfs(nx, ny)
                if childCount == 0 or count == 0:
                    count = 0
                else:
                    count += childCount
        return count

        
    def _inArea(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c

    def _atEdge(self, x, y):
        return x == 0 or x == self._r - 1 or y == 0 or y == self._c - 1

s = Solution()


print(s.numEnclaves([[0,0,0,1,1,1,0,1,0,0],
                     [1,1,0,0,0,1,0,1,1,1],
                     [0,0,0,1,1,1,0,1,0,0],
                     [0,1,1,0,0,0,1,0,1,0],
                     [0,1,1,1,1,1,0,0,1,0],
                     [0,0,1,0,1,1,1,1,0,1],
                     [0,1,1,0,0,0,1,1,1,1],
                     [0,0,1,0,0,1,0,1,0,1],
                     [1,0,1,0,1,1,0,0,0,0],
                     [0,0,0,0,1,1,0,0,0,1]]))