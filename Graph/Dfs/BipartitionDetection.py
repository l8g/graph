import sys
sys.path.insert(0, "../Expression")

from Graph import Graph

class BipartitionDetection():

    def __init__(self, g):
        self._g = g
        self._visited = [False] * g.v()
        self._colors = [-1] * g.v()
        self._isBipartite = True
        for v in range(g.v()):
            if not self._visited[v]:
                if not self._dfs(v, 0):
                    self._isBipartite = False
                    break

    def _dfs(self, v, color):
        self._visited[v] = True
        self._colors[v] = color
        for w in self._g.adj(v):
            if not self._visited[w]:
                if not self._dfs(w, 1 - color):
                    return False
            elif self._colors[w] == self._colors[v]:
                return False
        return True

    def isBipartite(self):
        return self._isBipartite


if __name__ == "__main__":
    g = Graph('g.txt')
    bd = BipartitionDetection(g)
    print(bd.isBipartite())

    g2 = Graph("g2.txt")
    bd2 = BipartitionDetection(g2)
    print(bd2.isBipartite())

    g3 = Graph("g3.txt")
    bd3 = BipartitionDetection(g3)
    print(bd3.isBipartite())
