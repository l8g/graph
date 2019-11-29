# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "../Expression")
from collections import deque
from Graph import Graph

class SingleSourceShortestPath():

    def __init__(self, g, s):
        self._g = g
        self._s = s
        self._visited = [False] * g.v()
        self._pre = [-1] * g.v()
        self._dis = [-1] * g.v()
        self._bfs(s)

    def _bfs(self, s):
        self._visited[s] = True
        self._pre[s] = s
        self._dis[s] = 0
        queue = deque()
        queue.append(s)

        while len(queue) > 0:
            curr = queue.popleft()

            for w in self._g.adj(curr):
                if not self._visited[w]:
                    self._visited[w] = True
                    self._pre[w] = curr
                    self._dis[w] = self._dis[curr] + 1
                    queue.append(w)
    
    def dis(self, t):
        return self._dis[t]

    def path(self, t):
        res = []
        if not self._visited[t]:
            return res
        while t != self._s:
            res.insert(0, t)
            t = self._pre[t]
        res.insert(0, self._s)
        return res

if __name__ == "__main__":
    g = Graph("g.txt")
    ssspath = SingleSourceShortestPath(g, 0)
    print(ssspath.dis(5), ssspath.path(5))
    print(ssspath.dis(2), ssspath.path(2))

