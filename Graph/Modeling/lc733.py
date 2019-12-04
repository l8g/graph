class Solution:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self._r = len(image)
        self._c = len(image[0])
        self._newColor = newColor
        self._image = image
        self._color = image[sr][sc]
        self._visited = [[False for _ in range(self._c)] for _ in range(self._r)]

        self._dfs(sr, sc)
        return image

    def _dfs(self, x, y):
        self._visited[x][y] = True
        self._image[x][y] = self._newColor

        for d in Solution.dirs:
            nx, ny = x + d[0], y + d[1]
            if self._inAdge(nx, ny) and not self._visited[nx][ny] and self._image[nx][ny] == self._color:
                self._dfs(nx, ny)

    def _inAdge(self, x, y):
        return x >= 0 and x < self._r and y >= 0 and y < self._c

