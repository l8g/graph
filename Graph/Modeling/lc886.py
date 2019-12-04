class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        if N < 3:
            return True
        g = [set() for _ in range(N)]
        for l in dislikes:
            g[l[0] - 1].add(l[1] - 1)
            g[l[1] - 1].add(l[0] - 1)

        self._g = g
        self._color = [-1] * N
        self._visited = [False] * N
        for i in range(N):
            if not self._visited[i] and not self._dfs(i, 0):
                return False
        return True

    def _dfs(self, v, color):
        self._visited[v] = True
        self._color[v] = color
        for w in self._g[v]:
            if not self._visited[w]:
                if not self._dfs(w, 1 - color):
                    return False
            elif self._color[w] == self._color[v]:
                return False
        return True

s = Solution()
s.possibleBipartition(4, [[1,2],[1,3],[2,4]])
