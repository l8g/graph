
import Graph

class CC():

    def __init__(self, g):
        self._g = g
        self._cccount = 0
        self._visited = [-1] * g.v()
        for v in range(g.v()):
            if self._visited[v] < 0:
                self._dfs(v)
                self._cccount += 1

    def _dfs(self, v):
        self._visited[v] = self._cccount
        for u in self._g.adj(v):
            if self._visited[u] < 0:
                self._dfs(u)


    def count(self):
        return self._cccount;

    def isConnect(self, u, v):
        return self._visited[u] == self._visited[v]


if __name__ == "__main__":
    g = Graph.Graph("g.txt")
    cc = CC(g)
    print(cc.count())
