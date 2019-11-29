# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "../Expression")
from Graph import Graph

from collections import deque

class BipartitionDetection():
    
    def __init__(self, g):
        self._g = g
        self._visited = [False] * g.v()
        self._colors = [0] * g.v()
        self._isBipartite = True

        for v in range(g.v()):
            if not self._visited[v]:
                if not self._bfs(v, 0):
                    self._isBipartite = False
                    break;

    def _bfs(self, v, color):
        self._visited[v] = True
        self._colors[v] = color
        queue = deque()
        queue.append(v)
        while len(queue) > 0:
            curr = queue.popleft();
            for w in self._g.adj(curr):
                if not self._visited[w]:
                    self._visited[w] = True
                    self._colors[w] = 1 - self._colors[curr]
                    queue.append(w)
                elif self._colors[curr] == self._colors[w]:
                    return False
        return True


        

    def isBipartite(self):
        return self._isBipartite;



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
