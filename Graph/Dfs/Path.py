import sys
sys.path.insert(0, "..")


from Expression.Graph import Graph

class Path():
    
    def __init__(self, g : Graph, s, t):
        self._g = g
        self._s = s;
        self._t = t;

        self._visited = [False] * g.v()
        self._pre = [-1] * g.v()
        self._pre[s] = s
        self._dfs(s)

    def _dfs(self, u):
        self._visited[u] = True
        if u == self._t:
            return True
        for v in self._g.adj(u):
            if not self._visited[v]:
                self._pre[v] = u
                if self._dfs(v):
                    return True
        return False

    def connected(self):
        return self._visited[self._t]

    def path(self):
        res = []
        if not self.connected():
            return res
        curr = self._t
        while curr != self._s:
            res.insert(0, curr)
            curr = self._pre[curr]
        res.insert(0, self._s)
        print(self._visited)
        return res

    
if __name__ == "__main__":
    g = Graph("g.txt")
    path = Path(g, 0, 5)
    print("0->5: ", path.path())

    path2 = Path(g, 0, 1)
    print("0->5: ", path2.path())
