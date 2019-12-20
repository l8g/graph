import sys
sys.path.insert(0, "../Expression")
from Graph import Graph

class FindBridges():

    def __init__(self, g):
        self._g = g
        self._ord = [0] * g.v()
        self._low = [0] * g.v()
        self._visited = [False] * g.v()
        self.count = 0
        self._bridges = list()
        self._dfs(0, 0)

    def _dfs(self, v, parent):
        self._visited[v] = True
        self._ord[v] = self.count
        self._low[v] = self._ord[v]
        self.count += 1

        for w in self._g.adj(v):
            if w != parent:
                if not self._visited[w]:
                    self._dfs(w, v)
                    self._low[v] = min(self._low[v], self._low[w])
                    if self._ord[v] < self._low[w]:
                        self._bridges.append((v, w))
                else:
                    self._low[v] = min(self._low[v], self._low[w])

    def getBridges(self):
        return self._bridges

g = Graph("g.txt")
fb = FindBridges(g)
print(fb.getBridges())

g = Graph("g2.txt")
fb = FindBridges(g)
print(fb.getBridges())


            
