class Solution:
    def findCircleNum(self, M) -> int:
        self._n = len(M)
        if self._n == 0:
            return 0

        self.M = M
        self._visited = [False] * self._n
        count = 0
        for i in range(self._n):
            if not self._visited[i]:
                self._dfs(i)
                count += 1
        return count

    def _dfs(self, i):
        self._visited[i] = True
        for j in range(self._n):
            if i != j and not self._visited[j] and self.M[i][j] == 1:
                self._dfs(j)

s = Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))