
from collections import deque
class Solution:
    def slidingPuzzle(self, board) -> int:
        self._visited = dict()
        self._target = ((1, 2, 3), (4, 5, 0))
        s = (tuple(board[0]), tuple(board[1]))
        if s == self._target:
            return 0
        return self._bfs(s)

    def _bfs(self, s):
        queue = deque()
        queue.append(s)
        self._visited[s] = 0
        
        while len(queue) > 0:
            curr = queue.popleft()
            nexts = self._getNexts(curr)
            for v in nexts:
                if v not in self._visited:
                    queue.append(v)
                    self._visited[v] = self._visited[curr] + 1
                    if v == self._target:
                        return self._visited[v]
        return -1

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def _getNexts(self, s):
        nexts = list()
        b = list([list(s[0]), list(s[1])])
        x = 0 if 0 in b[0] else 1
        y = b[x].index(0)
        for d in Solution.dirs:
            nx, ny = x + d[0], y + d[1]
            if self._inArea(nx, ny):
                b[x][y], b[nx][ny] = b[nx][ny], b[x][y]
                nexts.append(((tuple(b[0]), tuple(b[1]))))
                b[x][y], b[nx][ny] = b[nx][ny], b[x][y]
        return nexts

    def _inArea(self, x, y):
        return x >= 0 and x < 2 and y >= 0 and y < 3

s = Solution()
print(s.slidingPuzzle([[1,2,3],[4,0,5]]))
