import sys
sys.path.insert(0, '..')

from Expression.Graph import Graph

class CycleDetection():

    def __init__(self, g):
        self._g = g
        self._visited = [False] * g.v()

        self._hasCycle = False

        for v in range(g.v()):
            if not self._visited[v]:
                if self._dfs(v, v):
                    self._hasCycle = True
                    break
       
    def _dfs(self, v, parent):
        self._visited[v] = True
        for u in self._g.adj(v):
            if not self._visited[u]:
                self._dfs(u, v)
            elif u != parent:
                return True
        return False

    def hasCycle(self):
        return self._hasCycle

if __name__ == "__main__":
    g = Graph("g.txt")
    cd = CycleDetection(g)
    print(cd.hasCycle())

    g2 = Graph("g2.txt")
    cd2 = CycleDetection(g2)
    print(cd2.hasCycle())
