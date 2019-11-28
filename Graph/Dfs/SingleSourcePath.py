# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "..")

from Expression.Graph import Graph

class SingleSourcePath():
    
    def __init__(self, g : Graph, s : int):
        self._g = g
        self._s = s;
        self._g.validate(s)

        self._visited = [False] * g.v()
        self._pre = [-1] * g.v()

        self._pre[s] = s
        self._dfs(self._s)

    def _dfs(self, u):
        self._visited[u] = True
        for v in self._g.adj(u):
            if not self._visited[v]:
                self._pre[v] = u
                self._dfs(v)

    def isConnectedTo(self, t):
        self._g.validate(t)
        return self._visited[t]

    def path(self, t):
        res = []
        if not self.isConnectedTo(t):
            return res
        cur = t
        while cur != self._s:
            res.insert(0, cur)
            cur = self._pre[cur]
        res.insert(0, self._s)
        return res


if __name__ == "__main__":
    g = Graph("g.txt")
    sspath = SingleSourcePath(g, 0)
    print("0->5: ", sspath.path(5))
    print("0->4: ", sspath.path(4))